#!/usr/bin/python3
""" a module to define the place class """

import os

from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), nullable=False, primary_key=True),
    Column("amenity_id", String(60), ForeignKey("amenities.id"), nullable=False, primary_key=True)
)

class Place(BaseModel, Base):
    """ the place class inheriting from BaseModel """

    __tablename__ = "places"

    city_id: Mapped[str] = mapped_column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id: Mapped[str] = mapped_column(String(60), ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=True)
    description: Mapped[str] = mapped_column(String(1024), nullable=True)
    number_rooms: Mapped[int] = mapped_column(default=0)
    number_bathrooms: Mapped[int] = mapped_column(default=0)
    max_guest: Mapped[int] = mapped_column(default=0)
    price_by_night: Mapped[int] = mapped_column(default=0)
    latitude: Mapped[float] = mapped_column(nullable=True)
    longitude: Mapped[float] = mapped_column(nullable=True)
    amenity_id = []

    user: Mapped["User"] = relationship(back_populates="places")
    cities: Mapped["City"] = relationship(back_populates="places")
    reviews: Mapped["Review"] = relationship(back_populates="place", cascade="delete, delete-orphan")
    amenities: Mapped[List["Amenity"]] = relationship(secondary=place_amenity, viewonly=False, back_populates="place_amenities")

   

# place_amenity = Table(
#     "place_amenity",
#     Base.metadata,
#     Column("place_id", String(60), ForeignKey("places.id"), nullable=False),
#     Column("amenity_id", String(60), ForeignKey("amenities.id"), nullable=False)
# )