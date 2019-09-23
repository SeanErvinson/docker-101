import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my site"

@app.route("/cmd")
def cmd():
    return os.environ.get("CMD_ARGS") or ""

if __name__ == "__main__":
    app.run()