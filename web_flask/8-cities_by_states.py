#!/usr/bin/python3
""" a module to create a flask instance for my AirBnB app """

import os

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close():
    """ a function to call when a request has been handled
    this would close the session of the storage class """

    storage.close()


app.route("/cities_by_states")
def cities_by_states():
    """ a function to return all cities in all states """

    states = storage.all(State)

    return render_template("8-cities_by_state.html", states = states)

if __name__ == "__main__":
    app.run()