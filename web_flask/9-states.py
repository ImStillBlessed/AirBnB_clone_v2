#!/usr/bin/python3
"""
This script defines routes for a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

# storage.all()


@app.teardown_appcontext
def closing(arg=None):
    """
    Method For handling closing of each session
    """
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("states/<string:id>", strict_slashes=False)
def state_id_filter(id=None):
    """
    Displays state in html if the object is found with this id
    """
    path = '9-states.html'
    states = storage.all(State)
    return render_template(path, states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
