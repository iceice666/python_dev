import webbrowser
from win32api import ShellExecute

webbrowser.get('windows-default').open_new(
    "https://hackmd.io/@immortalmice/Hkj9s-CvU/https%3A%2F%2Fhackmd.io%2Fdz9INck7Qhyk5HJGS-oTDg")
ShellExecute(0, "open", "C:\\Users\\IceIc\\eclipse\\java-2020-06\\eclipse\\eclipse.exe", "", "", 0)
