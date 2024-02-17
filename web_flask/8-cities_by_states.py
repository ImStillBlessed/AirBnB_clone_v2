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


@app.route('/cities_by_states')
def states_list():
    """Render template with states
    """
    path = '8-cities_by_states.html'
    states = storage.all(State)

    return render_template(path, states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
