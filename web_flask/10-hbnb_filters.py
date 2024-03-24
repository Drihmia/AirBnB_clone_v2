#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask, render_template, url_for


HBNB = Flask(__name__)
HBNB.static_folder = 'static'


# task 11.
@HBNB.route("/hbnb_filters", strict_slashes=False)
def states():
    """states list that return a list of states using 'render
    template' and jinja"""
    
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)



# task 11.
@HBNB.teardown_appcontext
def teardown(_=None):
    """closing the storage and reload"""
    storage.close()


if __name__ == "__main__":
    """Entry point"""
    HBNB.run(host="0.0.0.0", port=5000, debug=True)
