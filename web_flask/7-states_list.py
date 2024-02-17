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
def closing():
    """
    Method For handling closing of each session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list(head):
    """
    Display a list of all State objects sorted by name in an HTML page.
    """
    states = sorted(storage.all("States").values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
