#!/usr/bin/python3
""" a module to test the user class """

from models import storage
from models.user import User
from unittest import TestCase

class TestUser(TestCase):
    """ a class to test the user class and its properties """

    user_1 = User()

    def test_user_dict(self):
        """ a method to check the dictionary of a class if it contains BaseModel attributes """

        self.assertIn("id", self.user_1.to_dict().keys())
        self.assertIn("created_at", self.user_1.to_dict().keys())
        self.assertIn("updated_at", self.user_1.to_dict().keys())

        user_1_key = f"{self.user_1.to_dict()['__class__']}.{self.user_1.id}"

        self.user_1.save()
        self.assertIn(user_1_key, storage.all().keys())
