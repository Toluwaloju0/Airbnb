#!/usr/bin/python3
""" a module to create a base for all the classes to be used"""

from datetime import datetime
from json import dumps
from uuid import uuid4

class BaseModel:
    """ the base class"""

    def __init__(self, *args, **kwargs):
        """ the initializer for the class attributes
        Args:
            args (list): an empty list for optional fixed parameters
            kwargs (dict): an dictionary containing the values to use to open a new account
        """

        # if there are kwarg arguments use them to initialize the class
        if len(kwargs) > 0:
            del kwargs["__class__"]
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(val))
                    continue
                setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ a special method to define the string for the class """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ a method to save a class """

        self.updated_at = datetime.now()
    
    def to_dict(self):
        """ a method to get the dictionary representation of a class """

        new_dict = {"__class__": self.__class__.__name__}
        new_dict.update(self.__dict__)
        print(self.__dict__)
        # convert the created_at and updated_at to strings
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
        