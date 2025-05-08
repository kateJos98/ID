from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        response = requests.get("http://usuarios-service:5001/usuarios")
        usuarios = response.json()
        lista = "".join(f"<li>{u['nombre']}</li>" for u in usuarios)
        return f"<h1>Usuarios:</h1><ul>{lista}</ul>"
    except Exception as e:
        return f"Error al obtener usuarios: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
