import os
import shutil


class packager:
    def __init__(self, p):
        self.package(p)

    def package(self, p):
        os.chdir(os.path.dirname(p))
        os.system(
            "pyinstaller {} -i ..\\icon.ico --specpath spec --distpath _@output -F -w".format(os.path.basename(p)))
        shutil.rmtree(os.path.dirname(p) + "\\build")
        shutil.rmtree(os.path.dirname(p) + "\\spec")
        shutil.rmtree(os.path.dirname(p) + "\\__pycache__")


packager("C:\\Users\\IceIc\\Desktop\\python[dev]\\pkg_test - (tools[dev])\\tools.py")
