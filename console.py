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

    not_updatable = ['id', 'created_at', 'updated_at']  # create a list for items which cant be updated
    
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

        args = args[0].split(" ")  # split the arguments by removing the spaces

        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        
        # create a dict to store the key and value pairs
        class_dict = {}
        for a in range (1, len(args)):
            if args[a].startswith(""):
                attribute = args[a].replace("\"", "").split("=")
                key, value = attribute[0], attribute[1]
            else:
                attribute = args[a].split("=")
                key = attribute[0]
                value = float(attribute[1]) if args[a].find(".") > 0 else int(attribute[1])
            class_dict[key] = value
        
        model = self.classes[args[0]](**class_dict)  # create a clas from the data provided
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
        all_instance = storage.all() if len(args) == 0 else storage.all(self.classes[args[0]])

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
        # get the value to be updated if it is surrounded by colons
        args = args[0].split('"')
        value = args[1] if len(args) >= 2 else None
        if value:
            value = int(value) if args[1].isdigit() else value

        args = args[0].split()  # deal with the rest of the argments
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

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
            value = int(args[3]) if args[3].isdigit() else args[3]
        if not value:
            print("** value missing **")
            return
        if args[2] in self.not_updatable:
            return

        setattr(class_instance, args[2], value)
        class_instance.save()

    def default(self, line):
        """ a method to handle commands not specified in the prompt
        Args:
            line: the command
        """

        args = line.split('.')
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** function missing **")
            return
        
        all_instance_dict = storage.all()  # get all instances

        if args[1] == "all":
            instance_list = []
            for key, instance_dict in all_instance_dict.items():
                if args[0] == key.split('.')[0]:
                    instance_list.append(str(self.classes[args[0]](**instance_dict)))
            if len(instance_list) == 0:
                print("** no instance found **")
            else:
                print(instance_list)
            return
        
        elif args[1] == "count":
            instance_count = 0
            for key, instance_dict in all_instance_dict.items():
                if args[0] == key.split('.')[0]:
                    instance_count += 1
            if instance_count == 0:
                print("** no instance found **")
            else:
                print(instance_count)
            return
        
        # strip the arguments of the ( and ) then split the second argument based on the '"' and
        # delete the empties then join it to the first arg 
        other_args = args[1].strip("(").strip(")").split("\"")
        unwanted = ["", ", "]  # characters which are not needed
        edited_args = [x.strip("(") for x in other_args if x not in unwanted]
        args = [args[0]] + edited_args

        if args[1] == "show":
            if len(args) < 3:
                print("** instance id missing **")
                return
            class_key = f"{args[0]}.{args[2]}"
            if class_key in all_instance_dict.keys():
                print(self.classes[args[0]](**all_instance_dict[class_key]))
            else:
                print("** no instance found **")
            return
            
        elif args[1] == "destroy":
            if len(args) < 3:
                print("** instance id missing **")
                return
            instance_key = f"{args[0]}.{args[2]}"
            if instance_key in all_instance_dict.keys():
                del all_instance_dict[instance_key]
                storage.update_file(all_instance_dict)
            else:
                print("** no instance found **")
            return

        elif args[1] == "update":
            if len(args) < 3:
                print("** instance id missing **")
                return
            instance_key = f"{args[0]}.{args[2]}"
            if instance_key in all_instance_dict.keys():
                class_instance = self.classes[args[0]](**all_instance_dict[instance_key])
                if len(args) < 4:
                    print("** attribute name missing **")
                    return
                if len(args) < 5:
                    print("** value missing **")
                    return
                if args[3] in self.not_updatable:
                    return
                args[4] = args[4].strip(", ")
                value = int(args[4]) if args[4].isdigit() else args[4]
                # set the attribute and print it
                setattr(class_instance, args[3], value)
                class_instance.save()
            else:
                print("** no instance found **")
            return



if __name__ == '__main__':
    HBNBCommand().cmdloop()
