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


@app.route('/python/(<text>)', strict_slashes=False)
def pythontext(text):
    """returns python message"""

    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
