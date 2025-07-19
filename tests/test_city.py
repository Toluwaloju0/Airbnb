#!/usr/bin/python3
""" a module to test the city class """

from models import storage
from models.city import City
from unittest import TestCase

class Testcity(TestCase):
    """ a class to test the city class and its properties """

    city_1 = City()

    def test_city_dict(self):
        """ a method to check the dictionary of a class if it contains BaseModel attributes """

        self.assertIn("id", self.city_1.to_dict().keys())
        self.assertIn("created_at", self.city_1.to_dict().keys())
        self.assertIn("updated_at", self.city_1.to_dict().keys())

        city_1_key = f"{self.city_1.to_dict()['__class__']}.{self.city_1.id}"

        self.city_1.save()
        self.assertIn(city_1_key, storage.all().keys())
