#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


hbnb = Flask(__name__)


# task 0.
@hbnb.route("/", strict_slashes=False)
def hello():
    """display “Hello hbnb!”"""
    return "Hello hbnb!"


# task 1.
@hbnb.route("/hbnb", strict_slashes=False)
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
@hbnb.teardown_appcontext
def teardown(_=None):
    """closing the storage and reload"""
    storage.close()


# task 8.
@hbnb.route("/states_list", strict_slashes=False)
def states_list():
    """states list that return a list of states using 'render
    template' and jinja"""

    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    """Entry point"""
    hbnb.run(host="0.0.0.0", port=5000)
