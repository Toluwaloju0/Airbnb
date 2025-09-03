#!/usr/bin/python3
""" a module to create an app using flask """

from flask import Flask, render_template, render_template_string
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close():
    """ a function to run at the end of every query to the app """

    storage.close()

@app.route("/states", strict_slashes=False)
@app.route("/states/id>", strict_slashes=False)
def state(id=None):
    """ a fuction to return all states or a particular state upon query """

    states = storage.all(State)

    if not id:
        return render_template("9-states.html")
    for key, value in states.items():
        if value.id == id:
            return render_template("9-states.html", states={key: value})
    return render_template_string("<h1>NOT FOUND </h1>", 404)
