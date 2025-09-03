#!/usr/bin/python3
""" a function to use flask for an wev application and to create an API """

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """ a function to print hello world when the home page is queried """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()