from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h3>Hello, world!<h3>"

@app.route("/sum/<int:a>/<int:b>")
def somma(a, b):
    return f"{a + b}"