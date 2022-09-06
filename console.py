#!/usr/bin/python3
"""The Console """
import cmd
import json
import models
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Console Class. """

    prompt = "(hbnb) "

    def emptyline(self, line):
        """Handles empty lines. """
        return Cmd.emptyline(self)

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """Handels to quit the command interprter with ctr + d

        Args:
            line (args): argument to for quiting the terminal.
        """
        print("bye, bye")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
