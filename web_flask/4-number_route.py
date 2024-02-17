#!/usr/bin/python3
"""
This script defines routes for a Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' when root URL is accessed.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when /hbnb URL is accessed.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    """
    Displays 'C' followed by the value of the text variable
    (replace underscore _ symbols with a space).
    """
    text = text.replace("_", " ")
    return "C " + text


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_cool(text="is cool"):
    """
    Displays 'Python' followed by the value of the text variable
    (replace underscore _ symbols with a space).
    The default value of text is 'is cool'.
    """
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """
    Displays “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
