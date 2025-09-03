#!/usr/bin/python3
""" a function to use flask for an wev application and to create an API """

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """ a function to print hello world when the home page is queried """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """ a function to display hello HBNB when it is queried """

    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """ a function to display the test provided to the function """

    text = text.replace("_", " ")
    return f"C {text}"

if __name__ == "__main__":
    app.run()