from flask import Flask


app = Flask(__name__)


@app.route('/')
def base():
    return 'This is a basic Flask application.'
