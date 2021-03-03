import sys

from src import setupvenv

try:
    import pyfiglet

except ModuleNotFoundError:
    setupvenv.install_packages("pyfiglet")

finally:
    import pyfiglet

def clear():
    sys.stdout.write("\x1b[2J\x1b[H")

def figlet(arg, color):
    print(Color(color)(pyfiglet.figlet_format(arg, font = "slant")))

class Color:
    COLORS = {
        "cyan": "\033[0;36m",
        "magenta": "\033[0;35m",
        "green": "\033[0;32m",
        "red": "\033[0;31m",
        "white": "\033[0;37m",
        "yellow": "\033[0;33m",
    }

    def __init__(self, color):
        try:
            self.prefix = self.COLORS[color.lower()]
        except AttributeError:
            raise ValueError("color must be a str")
        except KeyError:
            raise ValueError(f"unknow color, availables colors are {', '.join(self.COLORS)}")

    def __call__(self, text):
        return f"{self.prefix}{text} \033[0m"
