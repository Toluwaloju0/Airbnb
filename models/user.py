#!/usr/bin/python3
""" a module to create a user class for storing user data """

from models.base_model import BaseModel

class User(BaseModel):
    """ the user class inheriting from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""