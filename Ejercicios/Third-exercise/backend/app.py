import os
import time
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://ollama:11434")
MODEL = os.environ.get("MODEL", "tinyllama")


def wait_for_ollama():
    print("Esperando a Ollama...", flush=True)
    while True:
        try:
            requests.get(f"{OLLAMA_HOST}/api/tags", timeout=2)
            return
        except Exception:
            time.sleep(2)


def pull_model():
    r = requests.get(f"{OLLAMA_HOST}/api/tags")
    models = r.json().get("models", [])
    if any(m["name"].startswith(MODEL) for m in models):
        print(f"Modelo {MODEL} ya disponible.", flush=True)
        return

    print(f"Descargando modelo {MODEL}...", flush=True)
    with requests.post(
        f"{OLLAMA_HOST}/api/pull",
        json={"name": MODEL},
        stream=True
    ) as r:
        for line in r.iter_lines():
            if line:
                print(line.decode(), flush=True)
    print("Modelo listo.", flush=True)


wait_for_ollama()
pull_model()

app = Flask(__name__)
CORS(app)


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    history = data.get("history", [])

    messages = (
        [{"role": "system", "content": "Sos un asistente útil y conciso. Respondé siempre en el idioma del usuario."}]
        + history
        + [{"role": "user", "content": message}]
    )

    response = requests.post(
        f"{OLLAMA_HOST}/api/chat",
        json={"model": MODEL, "messages": messages, "stream": False, "options": {"temperature": 0.7}}
    )

    reply = response.json()["message"]["content"]
    return jsonify({"response": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
