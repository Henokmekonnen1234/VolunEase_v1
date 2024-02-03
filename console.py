#!/usr/bin/python3
"""
console.py will used to interact with the database
"""

import cmd
import shlex  # for splitting the line along spaces except in double quotes
import models

class VECommand(cmd.Cmd):
    """ VolunEase console """
    prompt = '(volunease)'

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def classes(self, cls=None):
        """Retrive classes from the import"""
        from models.base_model import BaseModel
        from models.event import Event
        from models.organization import Organization
        from models.volunteer import Volunteer
        if cls == "BaseModel":
            return BaseModel
        elif cls == "Event":
            return Event
        elif cls == "Organization":
            return Organization
        elif cls == "Volunteer":
            return Volunteer
        else:
            return None
    
    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if self.classes(args[0]):
            new_dict = self._key_value_parser(args[1:])
            instance = self.classes(args[0])(**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()
    
    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")
    
    def do_hash(self, arg):
        from models import utility
        print(utility.encrypt("password"))

if __name__ == '__main__':
    VECommand().cmdloop()