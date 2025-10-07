from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h3>Hello, world!<h3>"

@app.route("/square/<int:n>")
def square(n:int):
    return f"{n**2}"