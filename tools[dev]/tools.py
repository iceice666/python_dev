import sys
from threading import Thread
from tkinter import Button, Frame, Tk, Toplevel, Scrollbar, Text, RIGHT, DISABLED, END, Y
import json

try:
    from win32api import ShellExecute
except ModuleNotFoundError:
    import pywintypes
    from win32api import ShellExecute


def showError(e):
    root = Tk()
    w = 800
    h = 150
    root.title("Error!")
    root.geometry("%dx%d+%d+%d" % (w, h, (root.winfo_screenwidth() - w) / 2, (root.winfo_screenheight() - h) / 2))
    root.resizable(True, False)

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    t = Text(root, padx=5, pady=5, width=500, font="Consolas")
    t.insert(END, e)
    t.configure(state=DISABLED)
    t.pack()

    root.mainloop()


class tools:
    def __init__(self):
        self.ver = "1.0.0.0"

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
            return os.path.dirname(sys.executable)
        return os.path.dirname(__file__)

    def runCmd(self, i):
        Thread(target=lambda: ShellExecute(0, "open", self.appDIR + "projects\\{}".format(i), "", "", 0)).start()

    def loadSettings(self):
        ###          CONFIG          ###
        ###CHANGE YOUR LANG FILE HERE###
        lang = "zh_TW.json5"

        with open(self.appDIR + "data\\" + lang, "r", encoding="utf-8") as f:
            rjson = json.loads(f.read())
            self.UIs = rjson["ui"]
            self.projects = rjson["project"]

    ###       UI       ###

    def aboutAuthor(self):
        info = Toplevel()
        w = 400
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
        cmd = lambda: self.runCmd(obj["path"])
        return Button(root, command=cmd,
                      text=text, width=25).pack()

    def loadUI(self):
        btnList = []
        root = Tk()
        root.title(self.UIs["title"])
        root.resizable(False, True)
        w = 250
        h = 250
        root.geometry("%dx%d+%d+%d" % (w, h, (root.winfo_screenwidth() - w) / 2, (root.winfo_screenheight() - h) / 2))
        root.iconbitmap(self.appDIR + "icon.ico")

        frm1 = Frame(root).pack()
        Button(frm1, text="About", width=25, command=lambda: self.aboutAuthor(), relief="flat").pack(
            side=BOTTOM)

        frm_tools = Frame(root).pack()
        for i in self.projects.keys():
            b = self.makeBtn(frm_tools, i)
            btnList.append(b)

        root.mainloop()


# main
if __name__ == "__main__":
    try:
        tools()
    except BaseException as e:
        showError(e)
