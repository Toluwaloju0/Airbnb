#!/usr/bin/python3
""" a module to define the city class """

from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class City(BaseModel, Base):
    """ the city class inheriting from base """

    __tablename__ = "cities"

    state_id: Mapped[str] = mapped_column(String(60), ForeignKey("states.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)


    places: Mapped["Place"] = relationship(back_populates="cities", cascade="delete, delete-orphan")
    state: Mapped["State"] = relationship(back_populates="cities")