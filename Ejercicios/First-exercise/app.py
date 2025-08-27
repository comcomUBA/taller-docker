import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    environment = os.environ.get('ENVIRONMENT', 'production').lower()
    
    if environment == 'development':
        message = "¡Hola desde Flask en Docker! Modo desarrollo activado"
        print("Mensaje de desarrollo mostrado")  # Esto se imprimirá en la consola
    else:
        message = "¡Hola desde Flask en Docker!"
    
    return jsonify({"message": message, "environment": environment})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)