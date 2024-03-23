#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


# task 8.
@app.teardown_appcontext
def teardown(_=None):
    """closing the storage and reload"""
    storage.close()


# task 8.
@app.route("/states_list", strict_slashes=False)
def states_list():
    """states list that return a list of states using 'render
    template' and jinja"""

    states = storage.all(State)
    return render_template("7-states_list.html", States=states)


if __name__ == "__main__":
    """Entry point"""
    app.run(host="0.0.0.0", port=5000)
