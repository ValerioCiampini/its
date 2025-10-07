from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h3>Hello, world!<h3>"

@app.route("/about")
def show_description() -> str:
    return "Flask è un micro-framework Web scritto in Python, basato sullo strumento Werkzeug WSGI e con il motore di template Jinja2. È distribuito con licenza libera BSD. Flask è chiamato micro-framework perché ha un nucleo semplice ma estendibile."
