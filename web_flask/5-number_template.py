#!/usr/bin/python3

from flask import Flask, render_template
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


@app.route('/number/<int:n>')
def int_HBNB(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def int_template_HBNB(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')