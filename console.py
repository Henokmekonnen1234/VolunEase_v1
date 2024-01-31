#!/usr/bin/python3
"""
console.py will used to interact with the database
"""

import cmd

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
            return "class not found"
    
    def key_value(self, args=None):
        """This method retrive key value pairs from the string"""
        args_list = args.split(" ")
        return args_list
    
    def do_create(self, args):
        """This method will create classes from given string"""
        values = self.key_value(args)
        print(values)