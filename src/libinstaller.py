import subprocess
from . import tpdnlib

def install_packages(*packages):

    print(tpdnlib.Color("cyan")("Trying to install " + " ".join(packages)))
    subprocess.run(["python3", "-m", "pip", "install", *packages])
