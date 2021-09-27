import data
from tkinter import *
from tkinter import messagebox
from functools import partial  

def newWindow(name):
    window = Tk()
    window.title(name)
    window.geometry('600x400')
    window.resizable(width=True,height=True)
    return window

config = newWindow("Config") 


    

def donothing():
    print("hello")

def menubar(windows):
    
    def rightPopup(Event):
        menubar.tk_popup(Event.x_root,Event.y_root)
    #filemenue
    menubar = Menu(windows)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Reset", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit)
    #editmenu
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Delete All", command=donothing)
    #helpmenue
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    #selectmenue
    selectSetting = Menu(menubar, tearoff=0)
    selectSetting.add_command(label="Refree", command=donothing)
    selectSetting.add_command(label="Robots", command=donothing)
    selectSetting.add_command(label="Config", command=donothing)
    selectSetting.add_separator()
    selectSetting.add_command(label="open all", command=donothing)
    menubar.add_cascade(label="Select", menu=selectSetting)
    #event and show
    windows.config(menu=menubar)
    windows.bind("<Button-3>",rightPopup)

menubar(config)

config.mainloop()
