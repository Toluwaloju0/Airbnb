#!/usr/bin/python3
""" a module to define the review class """

from models.base_model import BaseModel

class Review(BaseModel):
    """ the review class inheriting from BaseModel """

    place_id = ""
    user_id = ""
    text = ""