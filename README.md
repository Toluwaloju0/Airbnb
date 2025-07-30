This is the Airbnb clone project it has a command line prompt made with cmd

open it by running `./console.py`
Models include:
    User
    Place
    State
    City
    Review
    Amenity

it can be used to perform the following commands

-- create <model>: this would create a new instance of a model and store it in a file. An id to the model instance is printed out
-- show <model> <id>: this would print out a model instance based on the id given
-- update <model> <id> <attr> <value>: this would update the value of the attribute of a model by its id and save it
-- delete <model> <id>: this would delete a model completely from it saved file
-- all <model>: this would print out all instances of every model saved. model is optional and if provided only instances of the provided model would be displayed

<model>.show <id>: same as show but different call syntax
<model>.all: same as all
<model>.update <id> <attr> <value>: same as update
<model>.delete <id>: same as delete