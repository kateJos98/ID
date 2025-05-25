from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/usuarios")
def get_usuarios():
    usuarios = [
        {"id": 1, "nombre": "Rosa"},
        {"id": 2, "nombre": "Luis"}
    ]
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
