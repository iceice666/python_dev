import os
from tkinter import Label,BOTTOM,Button,Frame,Tk




class tools():
    def __init__(self):
        self.DIRPATH=os.getcwd()+"\\"
        self.loadSettings()
        self.loadUI()

    def runCmd(self,i):
        os.system("{}projects\\{}\\main.bat".format(self.DIRPATH,self.projectPaths[i]))

    def loadSettings(self):
        self.projectPaths={}
        self.projectNames={}
        self.UIs={}

        lang=""

        with open(self.DIRPATH+"settings.ini","r",encoding="utf-8") as f:

            rlist=f.readlines()
            rlist_general=[]
            rlist_path=[]

        for i in rlist:
            if i.replace("\n","").startswith("#") is True:
                pass
            elif i == "\n":
                pass
            elif i.startswith("general.lang") is True:
                lang=(i.split("=")[1]).replace("\n","")
            elif i.startswith("project") is True:
                rlist_path.append(i.replace("\n",""))

        for i in rlist_path:
            self.projectPaths.setdefault(i.split("=")[0],i.split("=")[1])

        with open(self.DIRPATH+"lang\\"+lang+".lang","r",encoding="utf-8") as f:
            rlist=f.readlines()
            rlist_name=[]
            rlist_ui=[]

            for i in rlist:
                if i.replace("\n","").startswith("#") is True:
                    pass
                elif i == "\n":
                    pass
                elif i.startswith("project") is True:
                    rlist_name.append(i.replace("\n",""))
                elif i.startswith("ui") is True:
                    rlist_ui.append(i.replace("\n",""))

            for i in rlist_name:
                self.projectNames.setdefault(i.split("=")[0],i.split("=")[1])
            for i in rlist_ui:
                self.UIs.setdefault(i.split("=")[0],i.split("=")[1])



    def loadUI(self):
        root=Tk()
        root.title(self.UIs["ui.title"])
        root.geometry()

        if root.winfo_width() <250:
            w=250
        else:
            w=root.winfo_width()

        if root.winfo_height() <250:
            h=70
        else:
            h=root.winfo_height()

        root.geometry("%dx%d+%d+%d"%(w,h,(root.winfo_screenwidth()-w)/2,(root.winfo_screenheight()-h)/2))
        root.iconbitmap(self.DIRPATH+"icon.ico")

        frm1=Frame(root).pack()
        Label(frm1,text="Made by KSHSlime").pack(side=BOTTOM)

        frm_tools=Frame(root).pack()

        for i in self.projectPaths.keys():
            Button(frm_tools,text=self.projectNames[i],command=lambda: self.runCmd(i)).pack()



        root.mainloop()

#main
tools()