#!/usr/bin/python3
""" a module to define the state class """
import os

from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class State(BaseModel, Base):
    """ the state class inheriting from basemodel """

    __tablename__ = "states"

    name: Mapped[str] = mapped_column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities: Mapped[List["City"]] = relationship(back_populates="state", cascade="delete, delete-orphan")
    else:
        @property
        def cities(self):
            """ a getter to get all available cities in a state"""

            from models import storage
            from models.city import City

            all_cities = storage.all(City)

            cities = []
            for key, city in all_cities.items:
                if city.state_id == self.id:
                    cities.append(city)
            return cities
