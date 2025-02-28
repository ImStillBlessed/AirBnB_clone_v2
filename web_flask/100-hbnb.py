#!/usr/bin/python3
"""
This script defines routes for a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def closing(arg=None):
    """
    Method For handling closing of each session
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays the dynamic AirBnB page
    """
    path = '100-hbnb.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    user = storage.all(User)
    return render_template(path, states=states, 
                           amenities=amenities, places=places, user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
