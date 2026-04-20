import subprocess
import os
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("GREETING_NAME", "Hola Comcom! Primer Dockerfile hecho!")
    result = subprocess.run(["figlet", name], capture_output=True, text=True)
    return Response(result.stdout, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
