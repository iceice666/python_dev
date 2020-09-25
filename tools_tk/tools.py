import json
import os.path
import sys

import tools_tk.ui as _UI
import tools_tk.globalvar as gl

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
gl.init()
gl.set_value("DIR", DIR)


class tools:
    def __init__(self):
        self.ver = "1.0.1.0"

        self.appDIR = DIR
        self.UI_lang = {}
        self.projects = {}

    def tools(self):
        settings = "settings.json"

        with open(self.appDIR + "data\\" + settings, "r", encoding="utf-8") as f:
            rjson = json.loads(f.read())
            self.UI_lang = rjson["ui"]
            self.projects = rjson["project"]

        self.UI_tools()

    def error(self, e):
        self.UI_showError(e)

    def UI_tools(self):
        _UI.tools(self.ver, self.UI_lang, self.projects)

    def UI_showError(self, e):
        _UI.showError(e)


# main
if __name__ == "__main__":
    t = tools()
    try:
        t.tools()
    except SystemExit:
        pass
    except BaseException as e:
        t.error(e)
