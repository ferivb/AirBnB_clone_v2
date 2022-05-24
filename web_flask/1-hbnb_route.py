#!/usr/bin/python3
"""Starts a Flask web application
    where '/' displays 'Hello HBNB!'"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """ Prints Hello HBNB! on root '/'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """ Prints Hello HBNB! on root '/'"""
    return "HBNB!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
