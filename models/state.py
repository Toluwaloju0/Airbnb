#!/usr/bin/python3
""" a module to define the state class """

from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class State(BaseModel, Base):
    """ the state class inheriting from basemodel """

    __tablename__ = "states"

    name: Mapped[str] = mapped_column(String(128), nullable=False)
    cities: Mapped[List["State"]] = relationship(back_populates="state", cascade="delete, delete-orphan")

    @property
    def cities(self):
        """ a getter to get all available cities in a state"""

        return self.cities
