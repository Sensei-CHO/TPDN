import sys
from pathlib import Path
import importlib
import cmd


class Loader:
    def __init__(self):
        self.sources_path = Path() / "src"
        self.modules_path = Path() / "modules"
        self.sources = {}
        self.modules = {}

    def load_sources(self):
        for src in self.sources_path.glob("*.py"):
            src_name = ".".join(src.parts[:-1] + (src.stem,))
            self.sources[src.stem] = importlib.import_module(src_name)

    def load_modules(self):
        for module in self.modules_path.glob("*.py"):
            module_name = ".".join(module.parts[:-1] + (module.stem,))
            self.modules[module.stem] = importlib.import_module(module_name)

    def list_loaded(self):
        
        #list every sources
        #/!\no need to install sources/!\
        '''
        print("")
        print(self.sources["tpdnlib"].Color("yellow")("Installed sources are:"))
        for source in self.sources_path.glob("*.py"):
            print(self.sources["tpdnlib"].Color("cyan")(f" {source}"))
        '''

        print("")
        print(self.sources["tpdnlib"].Color("yellow")("Installed modules are:"))
        for module in self.modules_path.glob("*.py"):
            print(self.sources["tpdnlib"].Color("cyan")(f" {module}"))
        print("")

loader = Loader()
module = loader.modules
source = loader.sources
loader.load_sources()
loader.load_modules()


class PromptShell(cmd.Cmd):

    intro = source["tpdnlib"].Color("cyan")("Type help or ? to list commands.\n")
    prompt = source["tpdnlib"].Color("yellow")("TPDN>")

    def __init__(self):
        super(PromptShell, self).__init__()

    def do_close(self, arg):
        "Stop TPDN: close"
        source["tpdnlib"].clear()
        exit()

    def do_clear(self, arg):
        "Clear terminal: clear"
        source["tpdnlib"].clear()

    def do_echo(self, arg):
        "echo a string: echo HELLO."
        print(source["tpdnlib"].Color("cyan")(arg))

    def do_listloaded(self, arg):
        "list every installed sources and modules: ListModules"
        loader.list_loaded()

    def do_use(self, arg):
        "use a module: use helloworld"
        source["tpdnlib"].clear()

        try:
            module[arg].start()
        except KeyError:
            print(source["tpdn"].Color("red")("This modules don't exist or is not installed!"))

if __name__ == "__main__":
    source["tpdnlib"].clear()
    source["tpdnlib"].figlet("TPDN", "magenta")
    try:
        shell = PromptShell()
        shell.cmdloop()
    except KeyboardInterrupt:
        source["tpdnlib"].clear()
        pass
