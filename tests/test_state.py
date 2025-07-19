#!/usr/bin/python3
""" a module to test the state class """

from models import storage
from models.state import State
from unittest import TestCase

class Teststate(TestCase):
    """ a class to test the state class and its properties """

    state_1 = State()

    def test_state_dict(self):
        """ a method to check the dictionary of a class if it contains BaseModel attributes """

        self.assertIn("id", self.state_1.to_dict().keys())
        self.assertIn("created_at", self.state_1.to_dict().keys())
        self.assertIn("updated_at", self.state_1.to_dict().keys())

        state_1_key = f"{self.state_1.to_dict()['__class__']}.{self.state_1.id}"

        self.state_1.save()
        self.assertIn(state_1_key, storage.all().keys())
