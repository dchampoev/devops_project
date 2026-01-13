from flask import Flask
import socket

app = Flask(name)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/hostname")
def hostname():
    return f"Hostname: {socket.gethostname()}"

if name == "main":
    # Слушаме на порт 80, достъпен отвсякъде (0.0.0.0)
    app.run(host="0.0.0.0", port=80)
