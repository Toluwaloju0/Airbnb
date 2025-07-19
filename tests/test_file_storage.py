#!/usr/bin/python3
""" a module to test the file storage class in file_storage.py"""

from unittest import TestCase
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_file_storage(TestCase):
    """ the class to test the file storage class"""

    test_storage = FileStorage()

    def test_file_storage(self):
        """ a method to test the file storage creation """

        self.assertEqual(len(self.test_storage.all()), 0)
        self.base_1 = BaseModel()
        self.assertEqual(len(self.test_storage.all()), 1)