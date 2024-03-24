#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template, url_for


hbnb = Flask(__name__)
hbnb.static_folder = 'static'


# task 0.
@hbnb.route("/", strict_slashes=False)
def hello():
    """display “Hello hbnb!”"""
    return "Hello hbnb!"


# task 1.
@hbnb.route("/hbnb_0", strict_slashes=False)
def hello_hbnb():
    """display “hbnb”"""
    return "hbnb"


# task 2.
@hbnb.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """display “C ” followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


# task 3.
@hbnb.route("/python/", strict_slashes=False)
@hbnb.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """display “Python ”, followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


# task 4.
@hbnb.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


# task 5.
@hbnb.route("/number_template/<int:n>", strict_slashes=False)
def number_template_n(n):
    """display a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY"""
    return render_template("5-number.html", n=n)


# task 6.
@hbnb.route("/number_odd_or_even/<int:n>")
def number_odd_or_even_n(n):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY"""
    return render_template("6-number_odd_or_even.html", n=n)


# task 8.
@hbnb.route("/states_list", strict_slashes=False)
def states_list():
    """states list that return a list of states using 'render
    template' and jinja"""

    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


# task 9.
@hbnb.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """states list that return a list of states using 'render
    template' and jinja"""

    states = storage.all(State)
    return render_template("8-cities_by_states.html", States=states)


# task 10.
@hbnb.route("/states", strict_slashes=False)
def state():
    """states list that return a list of states using 'render
    template' and jinja"""

    states = storage.all(State)
    return render_template("9-states.html",
                           States=states, id="1234", found=False)


# task 10.
@hbnb.route("/states/<id>", strict_slashes=False)
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


# task 11.
@hbnb.route("/hbnb_filters", strict_slashes=False)
def states_filter():
    """states list that return a list of states using 'render
    template' and jinja"""

    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


# task 12.
@hbnb.route("/hbnb", strict_slashes=False)
def states():
    """states list that return a list of places, amenities and states with
    thier cities using 'render template' and jinja"""

    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


# task 8, 9, 11, 12.
@hbnb.teardown_appcontext
def teardown(_=None):
    """closing the storage and reload"""
    storage.close()


@hbnb.route("/index", strict_slashes=False)
def index_page():
    """Return the indexing page to browse all those path from
    one page"""
    return render_template("index.html")


@hbnb.route("/project_hbnb_static", strict_slashes=False)
def project_hbnb_static():
    """Return the indexing page to browse all those path from
    one page"""
    return render_template("project_hbnb_static.html")


if __name__ == "__main__":
    """Entry point"""
    hbnb.run(host="0.0.0.0", port=5000, debug=True)
