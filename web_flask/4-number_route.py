#!/usr/bin/python3
""" a function to use flask for an wev application and to create an API """

from flask import Flask, abort

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

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ a function to return the text given to the query """
    
    return f"Python {text.replace('_', ' ')}"

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """ a function to check if a query contains a num """
    
    if n.isdigit():
        return f"{n} is a number"
    abort(404)

if __name__ == "__main__":
    app.run()