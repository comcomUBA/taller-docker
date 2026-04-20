import os
from flask import Flask, request, redirect
import redis

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379, decode_responses=True)

NOTAS_DIR = "/app/notas"
os.makedirs(NOTAS_DIR, exist_ok=True)


@app.route("/", methods=["GET"])
def index():
    notas = r.lrange("notas", 0, -1)
    items = "".join(f"<li><a href='/nota/{n}'>{n}</a></li>" for n in notas)
    return f"""
    <html><body>
      <h1>Notas</h1>
      <form method="post" action="/nota">
        <input name="titulo" placeholder="Título" required>
        <textarea name="contenido" placeholder="Contenido" required></textarea>
        <button type="submit">Guardar</button>
      </form>
      <ul>{items}</ul>
    </body></html>
    """


@app.route("/nota", methods=["POST"])
def guardar():
    titulo = request.form["titulo"].strip()
    contenido = request.form["contenido"].strip()
    with open(f"{NOTAS_DIR}/{titulo}.txt", "w") as f:
        f.write(contenido)
    r.lpush("notas", titulo)
    return redirect("/")


@app.route("/nota/<titulo>")
def ver(titulo):
    path = f"{NOTAS_DIR}/{titulo}.txt"
    if not os.path.exists(path):
        return "Nota no encontrada", 404
    with open(path) as f:
        contenido = f.read()
    return f"<html><body><h1>{titulo}</h1><pre>{contenido}</pre><a href='/'>Volver</a></body></html>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
