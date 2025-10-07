from flask import Flask, url_for

app = Flask(__name__)
#app.run(debug = True, host = '127.0.0.1', port = 4000)

@app.route('/')
def home() -> str:
    return "<h3>Hello, world!<h3>"

@app.route('/user/<string:username>/age/<int:age>')
def show_user_profile(username:str, age:int) -> str|int:
    return f"Profilo di {username}, età: {age}"

@app.route("/post/<int:post_id>")
def show_post(post_id:int) -> int:
    return f"Post {post_id}"

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username = 'Jonh Doe', age = 0))
    print(url_for('show_post', post_id = 56))