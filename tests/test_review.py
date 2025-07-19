#!/usr/bin/python3
""" a module to test the review class """

from models import storage
from models.review import Review
from unittest import TestCase

class Testreview(TestCase):
    """ a class to test the review class and its properties """

    review_1 = Review()

    def test_review_dict(self):
        """ a method to check the dictionary of a class if it contains BaseModel attributes """

        self.assertIn("id", self.review_1.to_dict().keys())
        self.assertIn("created_at", self.review_1.to_dict().keys())
        self.assertIn("updated_at", self.review_1.to_dict().keys())

        review_1_key = f"{self.review_1.to_dict()['__class__']}.{self.review_1.id}"

        self.review_1.save()
        self.assertIn(review_1_key, storage.all().keys())
