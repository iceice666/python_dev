import sys
from threading import Thread
from tkinter import BOTTOM
from tkinter import Button, Frame, Tk
import json

try:
    from win32api import ShellExecute
except ModuleNotFoundError:
    import pywintypes
    from win32api import ShellExecute


class tools:
    def __init__(self):

        self.appDIR = self.app_path() + "\\"
        self.UIs = {}
        self.projects = {}
        self.loadSettings()
        self.loadUI()

    def app_path(self):
        import sys
        import os.path
        """Returns the base application path."""
        if hasattr(sys, 'frozen'):
            # Handles PyInstaller
            return os.path.dirname(sys.executable)  #使用pyinstaller打包后的exe目录
        return os.path.dirname(__file__)

    def runCmd(self, i):
        Thread(target=lambda: ShellExecute(0, "open", self.appDIR + "projects\\{}".format(i), "", "", 0)).start()

    def loadSettings(self):
        ###          CONFIG          ###
        ###CHANGE YOUR LANG FILE HERE###
        lang = "zh_TW.json"

        with open(self.appDIR + "data\\" + lang, "r", encoding="utf-8") as f:
            rjson = json.loads(f.read())
            self.UIs = rjson["ui"]
            self.projects = rjson["project"]

    def makeBtn(self, root, id):
        obj = self.projects[id]
        text = obj["name"]
        cmd = lambda: self.runCmd(obj["path"])
        return Button(root, command=cmd,
                      text=text, width=25).pack()

    def loadUI(self):
        root = Tk()
        btnList = []
        root.title(self.UIs["title"])

        frm1 = Frame(root).pack()
        Button(frm1, text="Made by KSHSlime", width=25, command=lambda: sys.exit(1), relief="flat").pack(side=BOTTOM)

        frm_tools = Frame(root).pack()
        for i in self.projects.keys():
            b = self.makeBtn(frm_tools, i)
            btnList.append(b)


        root.geometry()

        w = 250
        h = 250

        root.geometry("%dx%d+%d+%d" % (w, h, (root.winfo_screenwidth() - w) / 2, (root.winfo_screenheight() - h) / 2))
        root.iconbitmap(self.appDIR + "icon.ico")

        root.mainloop()


# main
tools()
