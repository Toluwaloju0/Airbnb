#!/usr/bin/python3
""" a module to create a base for all the classes to be used"""

from datetime import datetime
from models import storage
from uuid import uuid4
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import DateTime

class Base(DeclarativeBase):
    pass

class BaseModel:
    """ the base class"""

    id: Mapped[str] = mapped_column(String(60), primary_key=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ the initializer for the class attributes
        Args:
            args (list): an empty list for optional fixed parameters
            kwargs (dict): an dictionary containing the values to use to open a new account
        """

        # if there are kwarg arguments use them to initialize the class
        if len(kwargs) > 0 and kwargs.get("__class__"):
            del kwargs["__class__"]
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(val))
                    continue
                setattr(self, key, val)
        elif len(kwargs) > 0 and not kwargs.get("__class__"):
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for key, value in kwargs.items():
                setattr(self, key, value)
            storage.new(self)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ a special method to define the string for the class """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ a method to save a class """

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
    
    def to_dict(self):
        """ a method to get the dictionary representation of a class """

        new_dict = {"__class__": self.__class__.__name__}
        new_dict.update(self.__dict__)
        # convert the created_at and updated_at to strings
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        if new_dict.get("_sa_instance_state"):
            del new_dict["_sa_instance_state"]

        return new_dict

    def delete(self):
        """ a method to delete a instance of a class represented by self """

        storage.delete(self)