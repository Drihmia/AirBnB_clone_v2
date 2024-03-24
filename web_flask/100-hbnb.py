#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template, url_for


HBNB = Flask(__name__)
HBNB.static_folder = 'static'


# task 11.
@HBNB.route("/hbnb", strict_slashes=False)
def states():
    """states list that return a list of places, amenities and states with
    thier cities using 'render template' and jinja"""

    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


# task 11.
@HBNB.teardown_appcontext
def teardown(_=None):
    """closing the storage and reload"""
    storage.close()


if __name__ == "__main__":
    """Entry point"""
    HBNB.run(host="0.0.0.0", port=5000, debug=True)
