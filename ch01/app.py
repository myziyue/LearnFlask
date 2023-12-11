from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<center style='margin-top: 200px; font-size: 128px;'>Hello, World!</center>"
