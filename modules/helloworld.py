import sys
from pathlib import Path
import os
import cmd

sys.path.append(os.getcwd())
from src import tpdnlib

def clear():
    sys.stdout.write("\x1b[2J\x1b[H")

class PromptShell(cmd.Cmd):
    intro = tpdnlib.Color("cyan")("Type help or ? to list commands.\n")
    prompt = tpdnlib.Color("yellow")("helloworld>")

    def __init__(self):
        super(PromptShell, self).__init__()

    def do_back(self, arg):
        "Exit the module and return to TPDN: back"

        return True
    
    def do_clear(self, arg):
        "Clear the terminal: clear"

        print(tpdnlib.Color("cyan")("Exiting module..."))
        tpdnlib.clear()

    def do_helloworld(self, arg):
        "Print Hello World!: helloworld"
        print("")
        print(tpdnlib.Color("cyan")("Hello World!"))
        print("")

def start():

    tpdnlib.figlet("helloworld", "magenta")
    try:
        shell = PromptShell()
        shell.cmdloop()

    except KeyboardInterrupt:
        print(tpdnlib.Color("cyan")("Exiting module..."))
        clear()
