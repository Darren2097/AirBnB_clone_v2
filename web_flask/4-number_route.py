#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return Hello HBNB"""

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """returns C message"""

    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythontext(text="is cool"):
    """returns python message"""

    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def intstr(num):
    """returns int status message"""

    return "{} is a number".format(num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
