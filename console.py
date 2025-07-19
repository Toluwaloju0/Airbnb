#!/usr/bin/python3
""" a module to create a console gor the airbnb project """

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """the command line class """

    prompt = "(hbnb)"
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "City": City,
            "Review": Review,
            "Amenity": Amenity,
            "State": State
     } # a dict containing all available classes and the corresponding string name
    
    def emptyline(self):
        """  a method to define what happens when an empty line is pressed """

        pass

    def do_quit(self, *args):
        """ a method to describe what to do when is pressed """

        return True

    def do_EOF(self, *args):
        """ the command to run when EOF is reached or crtl + D is reached """

        print()
        return True

    def do_create(self, *args):
        """ a method to create a new class as specified in the args """

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        model = self.classes[args[0]]()
        model.save()
        print(model.id)
        return

    def do_show(self, *args):
        """ a method to print a class instance based on the id """

        if len(args) == 0:
            print("** class name missing **")
            return
        args = args[0].split()
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        # get all class instances using storage instance
        all_instance = storage.all()
        key = f"{args[0]}.{args[1]}"

        instance_dict = all_instance.get(key) # isolate the main instance
        if instance_dict is None:
            print(" ** no instance found **")
            return

        # create an instance from the dictionary of the instance
        instance = self.classes[args[0]](**instance_dict)
        print(instance)

    def do_destroy(self, *args):
        """ a method to destroy a class instance based on its id """

        if len(args) == 0:
            print("** class name missing **")
            return
        args = args[0].split()
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        # get all class instances using storage all method
        all_instance = storage.all()
        key = f"{args[0]}.{args[1]}"

        instance_dict = all_instance.get(key) # isolate the main instance
        if instance_dict is None:
            print(" ** no instance found **")
            return

        # delete the instance from the dictionary and update the file accordingly
        del all_instance[key]
        storage.update_file(all_instance)

    def do_all(self, *args):
        """ a method to get a all instances of a class and print them """

        args = args[0].split()

        if len(args) > 0:
            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
                return

        # get all class instances using storage instance
        all_instance = storage.all()

        # create a list and save the instances classes to it
        class_list = []
        for key, instance_dict in all_instance.items():
            class_name = key.split('.')[0]
            class_list.append(str(self.classes[class_name](**instance_dict)))
        print(class_list)

    def do_update(self, *args):
        """ a method to update a class based on the arguments given """

        if len(args) == 0:
            print("** class name missing **")
            return
        args = args[0].split('"')
        value = args[1] if len(args) >= 2 else None
        args = args[0].split()
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        not_updatable = ['id', 'created_at', 'updated_at']  # create a list for items which cant be updated

        # get all instances and check for the instance to be updated
        all_instances = storage.all()
        key = f"{args[0]}.{args[1]}"

        instance_dict = all_instances.get(key)
        if instance_dict is None:
            print("** no instance found **")
            return
        class_instance = self.classes[args[0]](**instance_dict)

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if not value and len(args) > 3:
            value = args[3]
        if not value:
            print("** value missing **")
            return
        if args[2] in not_updatable:
            return

        setattr(class_instance, args[2], value)
        class_instance.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
