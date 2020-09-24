import json
import os.path
import sys
from tkinter import Tk, Scrollbar, Text, RIGHT, DISABLED, END, Y

from tools_tk import ui

try:
    from win32api import ShellExecute
except ModuleNotFoundError:
    import pywintypes
    from win32api import ShellExecute

global DIR
if hasattr(sys, 'frozen'):
    DIR = os.path.dirname(sys.executable)
else:
    DIR = os.path.dirname(__file__)
DIR += "\\"


def showError(e):
    root = Tk()
    w = 800
    h = 150
    root.title("Error!")
    root.geometry("%dx%d+%d+%d" % (w, h, (root.winfo_screenwidth() - w) / 2, (root.winfo_screenheight() - h) / 2))
    root.iconbitmap(DIR + "error.ico")
    root.resizable(False, False)

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    t = Text(root, padx=5, pady=5, width=500, font="Consolas")
    t.insert(END, e)
    t.configure(state=DISABLED)
    t.pack()

    root.mainloop()


class tools:
    def __init__(self):
        self.ver = "1.0.1.0"

        self.appDIR = DIR
        self.UIs = {}
        self.projects = {}
        self.loadSettings()

    def loadSettings(self):
        settings = "settings.json"

        with open(self.appDIR + "data\\" + settings, "r", encoding="utf-8") as f:
            rjson = json.loads(f.read())
            self.UIs = rjson["ui"]
            self.projects = rjson["project"]

    def retureArgs(self):
        return self.ver, self.UIs, self.projects


class ui(ui):
    args = tools().retureArgs()

    super.__init__(args[0], args[1], args[2])


# main
if __name__ == "__main__":

    try:
        tools()
    except SystemExit:
        pass
    except BaseException as e:
        showError(e)
