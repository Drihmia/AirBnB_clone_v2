#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


HBNB = Flask(__name__)


# task 8.
@HBNB.route("/cities_by_states", strict_slashes=False)
def states_list():
    """states list that return a list of states using 'render
    template' and jinja"""

    states = storage.all(State)
    return render_template("8-cities_by_states.html", States=states)


# task 8.
@HBNB.teardown_appcontext
def teardown(error):
    """closing the storage and reload"""
    storage.close()


if __name__ == "__main__":
    """Entry point"""
    HBNB.run(host="0.0.0.0", port=5000)
