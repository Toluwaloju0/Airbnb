#!/usr/bin/python3
""" a module  to create a class to save another class """

from json import dumps, loads


class FileStorage:
    """the class used to store other class instances to a file"""

    __file_path = "file.json"
    __object = {}

    def all(self, cls=None):
        """ a method to get all the instances of a class"""

        if cls is None:
            return self.__object
        cls_dict = {}
        for key in self.__object:
            if cls.__name__ == key.split(".")[0]:
                cls_dict[key] = self.__object[key]
        return cls_dict

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

    def delete(self, obj=None):
        """ a method to delete an objexct from the storage file"""

        if obj is None:
            return
        del self.__object[f"{obj.__class__.__name__}.{obj.id}"]
        self.update_file(self.__object)

    def close(self):
        """ a method to close the class instance """

        self.reload()
