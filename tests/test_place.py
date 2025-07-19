#!/usr/bin/python3
""" a module to test the place class """

from models import storage
from models.place import Place
from unittest import TestCase

class Testplace(TestCase):
    """ a class to test the place class and its properties """

    place_1 = Place()

    def test_place_dict(self):
        """ a method to check the dictionary of a class if it contains BaseModel attributes """

        self.assertIn("id", self.place_1.to_dict().keys())
        self.assertIn("created_at", self.place_1.to_dict().keys())
        self.assertIn("updated_at", self.place_1.to_dict().keys())

        place_1_key = f"{self.place_1.to_dict()['__class__']}.{self.place_1.id}"

        self.place_1.save()
        self.assertIn(place_1_key, storage.all().keys())
