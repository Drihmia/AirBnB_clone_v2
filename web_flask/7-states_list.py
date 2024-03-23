#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


HBNB = Flask(__name__)


# task 8.
@HBNB.route("/states_list/", strict_slashes=False)
def states_list():
    """states list"""
    states = storage.all(State)
    return render_template("7-states_list.html", States=states)


# task 8.
@HBNB.teardown_appcontext
def storage_close(error=None):
    """closing the storage and reload"""
    storage.close()


if __name__ == "__main__":
    """Entry point"""
    HBNB.run(host="0.0.0.0", port=5000)
