import os.path
import sys
from threading import Thread
from tkinter import Toplevel, END, DISABLED, Button, Tk, Scrollbar, RIGHT, Frame, BOTTOM, Text, Y

from win32api import ShellExecute

global DIR
if hasattr(sys, 'frozen'):
    DIR = os.path.dirname(sys.executable)
else:
    DIR = os.path.dirname(__file__)
DIR += "\\"


class tools:
    def __init__(self, ver, UIs, prj):
        self.ver = ver
        self.UIs = UIs
        self.projects = prj
        self.appDIR = DIR

        self.loadUI()

    def runCmd(self, i):
        Thread(target=lambda: ShellExecute(0, "open", self.appDIR + "projects\\{}".format(i), "", "", 0)).start()

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


class showError:
    def __init__(self, e):
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
