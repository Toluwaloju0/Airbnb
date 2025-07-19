#!/usr/bin/python3
""" a module to test the amenity class """

from models import storage
from models.amenity import Amenity
from unittest import TestCase

class Testamenity(TestCase):
    """ a class to test the amenity class and its properties """

    amenity_1 = Amenity()

    def test_amenity_dict(self):
        """ a method to check the dictionary of a class if it contains BaseModel attributes """

        self.assertIn("id", self.amenity_1.to_dict().keys())
        self.assertIn("created_at", self.amenity_1.to_dict().keys())
        self.assertIn("updated_at", self.amenity_1.to_dict().keys())

        amenity_1_key = f"{self.amenity_1.to_dict()['__class__']}.{self.amenity_1.id}"

        self.amenity_1.save()
        self.assertIn(amenity_1_key, storage.all().keys())
