import sys
from threading import Thread
from tkinter import BOTTOM
from tkinter import Button, Frame, Tk

from win32api import ShellExecute
import json


class tools:
    def __init__(self):
        # self.DIRPATH=os.getcwd()+"\\"
        self.UIs = {}
        self.projects = {}
        self.loadSettings()
        self.loadUI()

    def runCmd(self, i):
        Thread(target=lambda: ShellExecute(0, "open", "projects\\{}".format(i), "", "", 0)).start()

    def loadSettings(self):
        ###          CONFIG          ###
        ###CHANGE YOUR LANG FILE HERE###
        lang = "zh_TW.json"

        with open("data\\" + lang, "r", encoding="utf-8") as f:
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

        '''
        ###ADD BUTTON##
        ###format:
        ###but_<project name> = Button(frm_tools, text=self.projectNames["project.<project name>"],
        ###                  command=lambda: self.runCmd("<project path>"), width=25).pack()
        but_mod_dev = Button(frm_tools, text=self.projectNames["project.mod_dev"],
                             command=lambda: self.runCmd("mod_dev\\mod_dev.py"), width=25).pack()
        but_py_dev = Button(frm_tools, command=lambda: self.runCmd("py_dev\\py_dev.py"),
                            text=self.projectNames["project.py_dev"], width=25).pack()
        ##############################################################################################
        '''
        root.geometry()

        w = 250
        h = 250

        root.geometry("%dx%d+%d+%d" % (w, h, (root.winfo_screenwidth() - w) / 2, (root.winfo_screenheight() - h) / 2))
        root.iconbitmap("icon.ico")

        root.mainloop()


# main
tools()
