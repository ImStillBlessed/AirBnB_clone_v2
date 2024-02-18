#!/usr/bin/python3
"""
This script defines routes for a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def closing(arg=None):
    """
    Method For handling closing of each session
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filter():
    """
    Displays the dynamic AirBnB page
    """
    path = '10-hbnb_filters.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(path, states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
