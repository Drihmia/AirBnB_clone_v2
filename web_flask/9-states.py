#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


HBNB = Flask(__name__)


# task 10.
@HBNB.route("/states", strict_slashes=False)
def states():
    """states list that return a list of states using 'render
    template' and jinja"""

    states = storage.all(State)
    return render_template("9-states.html",
                           States=states, id="1234", found=False)


# task 10.
@HBNB.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """states list that return a list of cities if state's id found
    using 'render template' and jinja"""
    states = storage.all(State)
    found = False

    key = f"State.{id}"
    if (key in states.keys()):
        found = True
    state_obj = states.get(key, "Not Found!")
    return render_template("9-states.html",
                           States=state_obj, idd=id, found=found)


# task 10.
@HBNB.teardown_appcontext
def teardown(_=None):
    """closing the storage and reload"""
    storage.close()


if __name__ == "__main__":
    """Entry point"""
    HBNB.run(host="0.0.0.0", port=5000)
