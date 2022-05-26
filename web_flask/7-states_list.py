#!/usr/bin/python3
"""Starts a Flask web application
    Using storage engine"""
from flask import Flask, escape, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays the states from the storage engine
    States are sorted by name."""
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(self):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
