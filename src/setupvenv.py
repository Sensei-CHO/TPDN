import venv
from pathlib import Path
import os
import subprocess
from . import tpdnlib

p = Path(__file__).parents[1] / "venv"
print(p)

if not p.is_dir():
    print(tpdnlib.Color("yellow")("Setting up venv..."))
    venv.EnvBuilder(with_pip=True).create(p)

def install_packages(*packages):
    
    if os.name == "nt":
        pip_path = p / "Scripts" / "pip.exe"

    else:
        pip_path = p / "bin" / "pip"
    
    subprocess.run([pip_path , "install", " ".join(packages)])
