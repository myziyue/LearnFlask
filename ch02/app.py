from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return f"<center style='margin-top: 200px; font-size: 128px;'>Hello, Index Page!</center>"


@app.route('/login')
def login():
    return 'login'


@app.route("/<name>")
def hello(name):
    return f"<center style='margin-top: 200px; font-size: 128px;'>Hello, {escape(name)}!</center>"


@app.route("/post/<int:post_id>")
def post(post_id):
    return f"<center style='margin-top: 200px; font-size: 128px;'>Post Page! #{escape(post_id)}!</center>"


@app.route("/path/<path:subpath>")
def show_subpart(subpath):
    return f"<center style='margin-top: 200px; font-size: 128px;'>Subpath Page! Path: `{escape(subpath)}`!</center>"


with app.test_request_context():
    print(url_for("index"))
    print(url_for("hello", name="Evan Bee"))
    print(url_for("login"))
    print(url_for("post", post_id=123))
    print(url_for("login", next='/'))
    print(url_for("show_subpart", subpath="abc/test/123"))
