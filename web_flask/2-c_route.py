#!/usr/bin/python3
"""a script that starts a Flask web application:
    My web application will be listening on 0.0.0.0, port 5000
    Routes:
        -> /: display “Hello HBNB!”
        -> /hbnb: display “HBNB”
        -> /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
        """
from flask import Flask

hbnb = Flask(__name__)


# task 0.
@hbnb.route("/", strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return "hello HBNB!"


# task 1.
@hbnb.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """display “HBNB”"""
    return "HBNB"


# task 2.
@hbnb.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ display “C ” followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    """entry point"""
    hbnb.run()
