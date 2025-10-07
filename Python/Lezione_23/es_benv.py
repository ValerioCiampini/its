from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h3>Hello, world!<h3>"

@app.route("/user/<string:username>")
def benvenuto(username:str) -> str:
    return f"Benvenuto {username}"