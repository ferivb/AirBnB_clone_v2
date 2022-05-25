#!/usr/bin/python3
"""Starts a Flask web application
    where '/' displays 'Hello HBNB!'"""
from flask import Flask, escape, render_template
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
    """ something something python something"""
    text = text.replace("_", " ")
    return "Python %s" % escape(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ Checks if a variable is an int"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_n_template(n):
    """ Uses a template"""
    return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
