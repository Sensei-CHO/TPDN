import sys
from pathlib import Path
import os
import cmd


from src import tpdnlib
from src import setupvenv

try:
    import <modules>

except ModuleNotFoundError:
    setupvenv.install_packages("<modules>")

finally:
    import <modules>


class PromptShell(cmd.Cmd):
    intro = tpdnlib.Color("cyan")("Type help or ? to list commands.\n")
    prompt = tpdnlib.Color("yellow")("<modulename>>")

    def __init__(self):
        super(PromptShell, self).__init__()

    def do_back(self, arg):
        "Exit the module and return to TPDN: back"

        return True
    
    def do_clear(self, arg):
        "Clear the terminal: clear"

        print(tpdnlib.Color("cyan")("Exiting module..."))
        tpdnlib.clear()

    def do_commandname(self, arg):
        "some description: command"

def start():

    tpdnlib.figlet("<modulename>", "magenta")
    try:
        shell = PromptShell()
        shell.cmdloop()

    except KeyboardInterrupt:
        print(tpdnlib.Color("cyan")("Exiting module..."))
        clear()
        
