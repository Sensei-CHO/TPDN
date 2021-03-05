import subprocess
from . import tpdnlib

def install_packages(*packages):

    print(tpdnlib.Color("cyan")("Trying to install " + " ".join(packages)))
    subprocess.run(["pip", "install", *packages])
