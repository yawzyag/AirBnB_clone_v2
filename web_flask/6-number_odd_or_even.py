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


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even_HBNB(n):
    if n % 2 == 0:
        val = "even"
    else:
        val = "odd"
    return render_template('6-number_odd_or_even.html', n=n, val=val)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
