from lib.settings import *
from lib.operations import *
from tkinter import *
from tkinter import filedialog

def build(master: Misc, typeApp: BUILD_TYPE):
    if typeApp == BUILD_TYPE.MAIN:
        header = Label(master, text=NAME_WINDOWS.MAIN, font=FONTS_WEIGHT.HEADING)
        labelInput = Label(master, text="Flash drive")
        inputFlashDrive = Entry(master)
        header.pack()
        labelInput.pack()
        inputFlashDrive.pack()