#!/usr/bin/python3
""" a module to define the city class """

from models.base_model import BaseModel

class City(BaseModel):
    """ the city class inheriting from base """

    state_id = ""
    city = ""