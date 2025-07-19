#!/usr/bin/python3
""" a module  to create a class to save another class """

from json import dumps, loads


class FileStorage:
    """the class used to store other class instances to a file"""

    __file_path = "file.json"
    __object = {}

    def all(self):
        """ a method to get all the instances of a class"""

        return self.__object

    def new(self, obj):
        """ a method to save a new object to a the __object dictionary
        Args:
            obj: the object to be saved
        """

        self.__object.update({f"{obj.__class__.__name__}.{obj.id}": obj.to_dict()})

    def save(self):
        """ a method to save the __object attribute to a file """

        with open(self.__file_path, "w") as file:
            file.write(dumps(self.__object))
    
    def reload(self):
        """ a method to get attributes from the saved file to __objects """

        try:
            with open(self.__file_path, "r") as file:
                content = file.read()
                self.__object = loads(content)
        except FileNotFoundError:
            pass

    def update_file(self, cls_dict):
        """ a method to update the file with a new dictionary especially after a delete """

        self.__object = cls_dict
        with open(self.__file_path, "w") as file:
            file.write(dumps(cls_dict))