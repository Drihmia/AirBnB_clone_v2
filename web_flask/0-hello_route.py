#!/usr/bin/python3
"""a script that starts a Flask web application:
    My web application will be listening on 0.0.0.0, port 5000
    Routes:
        -> /: display “Hello HBNB!”
        """
from flask import Flask
hbnb = Flask(__name__)


# task 0.
@hbnb.route("/", strict_slashes=False)
def hello_hbnb():
    """display “Hello HBNB!”"""
    return "hello HBNB!"


if __name__ == "__main__":
    """display “Hello HBNB!”"""
    hbnb.run()
