import json
from threading import Thread
from tkinter import Button, Frame, Tk, Toplevel, Scrollbar, Text, RIGHT, DISABLED, END, Y, BOTTOM

try:
    from win32api import ShellExecute
except ModuleNotFoundError:
    import pywintypes
    from win32api import ShellExecute

import sys
import os.path

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
        self.loadUI()

    def runCmd(self, i):
        Thread(target=lambda: ShellExecute(0, "open", self.appDIR + "projects\\{}".format(i), "", "", 0)).start()



    def loadSettings(self):
        settings = "settings.json"

        with open(self.appDIR + "data\\" + settings, "r", encoding="utf-8") as f:
            rjson = json.loads(f.read())
            self.UIs = rjson["ui"]
            self.projects = rjson["project"]

    #       UI       #

    def aboutAuthor(self):
        info = Toplevel()
        w = 430
        h = 150
        info.resizable(False, False)
        info.title("Credits")
        info.geometry("%dx%d+%d+%d" % (w, h, (info.winfo_screenwidth() - w) / 2, (info.winfo_screenheight() - h) / 2))

        t = Text(info, padx=5, pady=5, font="微軟正黑體")
        t.pack()
        t.insert(END, """
            Tools.exe [ver {ver}]

            Programmer - iceice666
            UI Designer KSHSlime

            """.format(ver=self.ver))
        t.configure(state=DISABLED)

    def makeBtn(self, root, project_id):
        obj = self.projects[project_id]
        text = obj["name"]

        def cmd(): return self.runCmd(obj["path"])

        return Button(root, command=cmd, text=text, width=280).pack()

    def loadUI(self):
        btnList = []
        root = Tk()
        root.title(self.UIs["title"])
        #root.resizable(False, False)
        w = 280
        h = 280
        root.geometry("%dx%d+%d+%d" % (w, h, (root.winfo_screenwidth() - w) / 2, (root.winfo_screenheight() - h) / 2))
        root.iconbitmap(self.appDIR + "icon.ico")

        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)

        frm1 = Frame(root).pack()
        Button(frm1, text="EXIT", width=25, command=lambda: sys.exit(0), relief="flat").pack(side=BOTTOM)
        Button(frm1, text="About", width=25, command=lambda: self.aboutAuthor(), relief="flat").pack(side=BOTTOM)

        frm_tools = Frame(root).pack()
        for i in self.projects.keys():
            b = self.makeBtn(frm_tools, i)
            btnList.append(b)

        root.mainloop()


# main
if __name__ == "__main__":

    try:
        tools()
    except SystemExit:
        pass
    except BaseException as e:
        showError(e)
