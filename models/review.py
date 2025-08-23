#!/usr/bin/python3
""" a module to define the review class """

from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Review(BaseModel, Base):
    """ the review class inheriting from BaseModel """

    __tablename__ = "reviews"

    place_id: Mapped[str] = mapped_column(String(60), ForeignKey("places.id"), nullable=False)
    user_id: Mapped[str] = mapped_column(String(60), ForeignKey("users.id"), nullable=False)
    text: Mapped[str] = mapped_column(String(1024), nullable=False)

    user: Mapped["User"] = relationship(back_populates="reviews")
    place: Mapped["Place"] = relationship(back_populates="reviews")

    @property
    def reviews(self, place_id):
        """ a method to get all reviews of a given place """

        review_list = []
        for review in self.reviews:
            if review.place_id == place_id:
                review_list.append(review)
        return review_list