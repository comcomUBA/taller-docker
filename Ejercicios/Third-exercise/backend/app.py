import os
import time
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://ollama:11434")
MODEL = os.environ.get("MODEL", "qwen2:0.5b")


def wait_for_ollama():
    print("Esperando a Ollama...", flush=True)
    while True:
        try:
            requests.get(f"{OLLAMA_HOST}/api/tags", timeout=2)
            return
        except Exception:
            time.sleep(2)


wait_for_ollama()

app = Flask(__name__)
CORS(app)


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


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
