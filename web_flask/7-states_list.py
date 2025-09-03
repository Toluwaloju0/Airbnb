#!/usr/bin/python3
""" a module to start a flask app to return states objects """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown():
    """ a function to close the database connection """

    storage.close()


@app.route("/state_list", strict_slashes=True)
def state_list():
    """ a function to return all states to the user """

    states = storage.all(State)

    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run()
