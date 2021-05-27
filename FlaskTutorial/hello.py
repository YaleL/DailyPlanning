from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

"""@app.route("/<name>/<test>")
def hello(name, test):
    return f"Hello, {escape(name)} {escape(test)}!"
"""