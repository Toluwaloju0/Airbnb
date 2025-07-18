#!/usr/bin/python3
""" a module to test the base model class"""

from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from unittest import TestCase

class TestBaseModel(TestCase):
    """ the test class for the base model """

    base_1, base_2 = BaseModel(), BaseModel()

    def test_datetime(self):
        """ the test to check the base model created_at and updated_at attributes """

        self.assertNotEqual(self.base_1.updated_at, self.base_1.created_at)
        sleep(2)
        self.base_1.save()
        self.assertNotEqual(self.base_1.updated_at, self.base_1.created_at)

    def test_attributes_type(self):
        """ a method to test the type of the attributes """

        self.assertIsInstance(self.base_1.created_at, datetime)
        self.assertIsInstance(self.base_1.updated_at, datetime)
        self.assertIsInstance(self.base_1.id, str)
        self.assertIsInstance(self.base_1.to_dict(), dict)
        self.assertIsInstance(self.base_1.to_dict()["created_at"], str)
        self.assertIsInstance(self.base_1.to_dict()["updated_at"], str)

    def test_properties_in_created_class(self):
        """ a method to check the properties present in the returned dict and their types """

        base_1_dict = self.base_1.to_dict()
        self.assertIn("created_at", base_1_dict)
        self.assertIn("id", base_1_dict)
        self.assertIn("updated_at", base_1_dict)
        self.assertIn("__class__", base_1_dict)

    def test_id_difference(self):
        """ a method to test if the id generated is different for each class"""

        self.assertNotEqual(self.base_1.id, self.base_2.id)

    def test_creation_with_dictionary(self):
        """ a method to create a class with a dict"""

        base_2_dict = self.base_2.to_dict()
        self.base_3 = BaseModel(**base_2_dict)
        self.assertEqual(self.base_3.id, self.base_2.id)
        self.assertEqual(self.base_2.created_at, self.base_3.created_at)
        self.assertEqual(self.base_2.updated_at, self.base_3.updated_at)
        self.assertIsNot(self.base_2, self.base_3)

    def test_dictionary_class_attributes(self):
        """ a method to confirm that the attributes of the created class
        are well defined"""

        base_2_dict = self.base_2.to_dict()
        self.base_3 = BaseModel(**base_2_dict)
        self.assertIsInstance(self.base_3.created_at, datetime)
        self.assertIsInstance(self.base_3.updated_at, datetime)
        self.assertIsInstance(self.base_3.id, str)
