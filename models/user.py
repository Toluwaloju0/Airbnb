#!/usr/bin/python3
""" a module to create a user class for storing user data """

from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(BaseModel, Base):
    """ the user class inheriting from BaseModel"""

    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(128), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    first_name: Mapped[str] = mapped_column(String(128), nullable=True)
    last_name: Mapped[str] = mapped_column(String(128), nullable=True)

    places: Mapped["Place"] = relationship(back_populates="user", cascade="delete, delete-orphan")
    reviews: Mapped["Review"] = relationship(back_populates="user", cascade="delete, delete-orphan")