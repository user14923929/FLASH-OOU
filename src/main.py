from lib.settings import *
from lib.build import build
from tkinter import *

try:
    mainApp = Tk()
    mainApp.geometry(f"{WINDOW_SIZES.MAIN_WINDOW.WIDTH}x{WINDOW_SIZES.MAIN_WINDOW.HEIGHT}")
    mainApp.resizable(RESIZABLE_THE_WINDOW, RESIZABLE_THE_WINDOW)
    mainApp.title(NAME_WINDOWS.MAIN)

    build(mainApp, BUILD_TYPE.MAIN)

    mainApp.mainloop()
except Exception:
    pass