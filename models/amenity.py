#!/usr/bin/python3
""" a module to define the amenity class """

from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

class Amenity(BaseModel, Base):
    """ the amenity class inheriting from BaseModel """

    __tablename__ = "amenities"

    name: Mapped[str] = mapped_column(String(128), nullable=False)

    place_amenities: Mapped[List["Place"]] = relationship(secondary=place_amenity, back_populates="amenities", viewonly=True)
