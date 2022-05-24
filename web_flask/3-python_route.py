#!/usr/bin/python3
"""Starts a Flask web application
    where '/' displays 'Hello HBNB!'"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """ Prints Hello HBNB! on root '/'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """ Prints HBNB! on '/hbnb'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_variable(text):
    """ displays variable 'text'! on '/c/'"""
    text = text.replace("_", " ")
    return "C %s" % escape(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    """ displays variable 'text'! on '/c/'"""
    text = text.replace("_", " ")
    return "Python %s" % escape(text)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
