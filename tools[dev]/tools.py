import sys
from threading import Thread
from tkinter import BOTTOM
from tkinter import Button, Frame, Tk

from win32api import ShellExecute


class tools:
    def __init__(self):
        # self.DIRPATH=os.getcwd()+"\\"
        self.UIs = {}
        self.projectNames = {}
        self.projectPaths = {}
        self.loadSettings()
        self.loadUI()

    def runCmd(self, i):
        Thread(target=lambda: ShellExecute(0, "open", "projects\\{}".format(i), "", "", 0)).start()

    def loadSettings(self):
        ###          CONFIG          ###
        ###CHANGE YOUR LANG FILE HERE###
        lang = "zh_TW.lang"

        with open("lang\\" + lang, "r", encoding="utf-8") as f:
            rlist = f.readlines()
            rlist_name = []
            rlist_ui = []

            for i in rlist:
                if i.replace("\n", "").startswith("#") is True:
                    pass
                elif i == "\n":
                    pass
                elif i.startswith("project") is True:
                    rlist_name.append(i.replace("\n", ""))
                elif i.startswith("ui") is True:
                    rlist_ui.append(i.replace("\n", ""))

            for i in rlist_name:
                self.projectNames.setdefault(i.split("=")[0], i.split("=")[1])
            for i in rlist_ui:
                self.UIs.setdefault(i.split("=")[0], i.split("=")[1])

    def makeBtn(self, root, path):
        return Button(root, command=lambda: self.runCmd(path),
                      text=self.projectNames["project.py_dev"], width=25).pack()

    def loadUI(self):
        root = Tk()
        root.title(self.UIs["ui.title"])

        frm1 = Frame(root).pack()
        Button(frm1, text="Made by KSHSlime", width=25, command=lambda: sys.exit(1), relief="flat").pack(side=BOTTOM)

        frm_tools = Frame(root).pack()
        self.makeBtn(frm_tools, "")

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
