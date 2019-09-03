#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb')
def route_HBNB():
    return 'HBNB'


@app.route('/c/<text>')
def text_HBNB(text):
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def pyt_HBNB(text="is cool"):
    s = """Python {zzz}"""
    return s.format(zzz=text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
