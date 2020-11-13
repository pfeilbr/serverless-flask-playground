from flask import Flask

import json
import os


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/env")
def env():
    return f"<pre>{json.dumps(dict(os.environ), indent=4, sort_keys=True)}</pre>"
