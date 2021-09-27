import data
from tkinter import *
from tkinter import messagebox
from functools import partial  
import os
import shutil





def save(id,name,value):
    loadPage()
    data.clearSetData(id.get())
    print(name.get())
    data.setDataValue(id.get(),name.get(),value.get())
    messagebox.showinfo("success","saved!!!!")

def newWindow(name):
    window = Tk()
    window.title(name)
    window.geometry('600x400')
    window.resizable(width=True,height=True)
    return window
def loadPage():
    load=newWindow("Load")
    def openLoad():
        path = os.path.join(os.getcwd(), 'data',listBox.get(ANCHOR))
        db_files = [f for f in os.listdir(path) if f.endswith('.db')]
        for x in db_files:
            shutil.copyfile(path+"/"+ x,os.getcwd()+"/"+x)
        print(listBox.get(ANCHOR))
    loadList=option()
    row1=PanedWindow(load)
    row1.pack(fill=BOTH,expand=0,side=TOP)
    listBox=Listbox(row1)
    if os.path.isdir('data'):
        print('data directory exist')
    else:
        os.mkdir('data')

    listName=os.listdir('data')

    print(os.getcwd())
    for x in listName:
        listBox.insert(END,x)
    row1.add(listBox)

    row2=PanedWindow(load)
    row2.pack(fill=BOTH,expand=0,side=TOP)
    loadSelect=Button(row2,text="load",command=openLoad)
    row2.add(loadSelect)

    row3=PanedWindow(load)
    row3.pack(fill=BOTH,expand=0,side=TOP)
    loadSelect=Button(row3,text="Next",command=load.destroy)
    row3.add(loadSelect)

    row4=PanedWindow(load)
    row4.pack(fill=BOTH,expand=0,side=TOP)
    loadSelect=Button(row4,text="Exit",command=exit)
    row4.add(loadSelect)
    load.mainloop()

def savePage():
    saveAs=newWindow("Save as...")
    
    def saveAsFunction():
        path = os.path.join(os.getcwd(), 'data',fileNameData.value.get())
        if os.path.isdir(path):
            print(path,'directory exist')
        else:
            os.mkdir(path)
        db_files = [f for f in os.listdir() if f.endswith('.db')]
        for x in db_files:
            shutil.copyfile(x, path+"/"+ x)
        
        print('saved',fileNameData.value.get())
    fileNameData=option()
    fileNameData.value = StringVar(saveAs)
    row1=PanedWindow(saveAs)
    row1.pack(fill=BOTH,expand=0,side=TOP)
    fileNameData.lable=Label(row1,text='Name: ')
    fileNameData.entry=Entry(row1,textvariable=fileNameData.value)
    row1.add(fileNameData.lable)
    row1.add(fileNameData.entry)

    row2=PanedWindow(saveAs)
    row2.pack(fill=BOTH,expand=0,side=TOP)
    saveAsButton=Button(row2,text="Save as",command=saveAsFunction)
    row2.add(saveAsButton)


    row3=PanedWindow(saveAs)
    row3.pack(fill=BOTH,expand=0,side=TOP)
    loadButton=Button(row3,text="Load",command=loadPage)
    row3.add(loadButton)

    row4=PanedWindow(saveAs)
    row4.pack(fill=BOTH,expand=0,side=TOP)
    closeButton=Button(row4,text="Exit",command=exit)
    row4.add(closeButton)

    saveAs.mainloop()



config = newWindow("Config") 
refree = newWindow("Refree")
robots = newWindow("Robots")


    

def donothing():
    print("do nothing harchi hichi nemigam eeee!!!!!")

def menubar(windows):
    
    def rightPopup(Event):
        menubar.tk_popup(Event.x_root,Event.y_root)
    #filemenue
    menubar = Menu(windows)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Reset", command=donothing)
    filemenu.add_command(label="Open", command=loadPage)
    filemenu.add_command(label="Save", command=savePage)
    filemenu.add_command(label="Save as...", command=savePage)
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
menubar(refree)
menubar(robots)
class option:
            lable=Label()
            value=0
            entry=Entry()
            optionmenu=0

# .........config
gameModeConfig=option()
gameModeConfig.value = StringVar(config)
gameModeConfig.value.set("Run in simulator") # default value
row1=PanedWindow(config)
row1.pack(fill=BOTH,expand=1,side=TOP)
gameModeConfig.lable=Label(row1,text=" Game Mode: ",font=("Tahoma",18),foreground="red")
row1.add(gameModeConfig.lable)
gameModeConfig.optionmenu=OptionMenu(row1, gameModeConfig.value, "Run in simulator", "Technical challenge", "Hardware challenge")
row1.add(gameModeConfig.optionmenu)

divisionConfig=option()
divisionConfig.value = StringVar(config)
divisionConfig.value.set("div A") # default value
divisionConfig.lable=Label(row1,text=" Division: ",font=("Tahoma",18),foreground="red")
row1.add(divisionConfig.lable)
divisionConfig.optionmenu=OptionMenu(row1, divisionConfig.value, "div A", "div B", "div OMID")
row1.add(divisionConfig.optionmenu)

row2=PanedWindow(config)
row2.pack(fill=BOTH,expand=1,side=TOP)
maxRobotConfig=option()
maxRobotConfig.value=IntVar(config)
maxRobotConfig.value.set(11)
maxRobotConfig.lable=Label(row2,text=" Max robots: ",font=("Tahoma",18),foreground="red")
row2.add(maxRobotConfig.lable)
maxRobotConfig.entry=Entry(row2,textvariable = maxRobotConfig.value)
row2.add(maxRobotConfig.entry)
distanceToBallInStopModeConfig=option()
distanceToBallInStopModeConfig.value=DoubleVar(config)
distanceToBallInStopModeConfig.value.set(500)
distanceToBallInStopModeConfig.lable=Label(row2,text=" Distance to ball in stop mode: ",font=("Tahoma",18),foreground="red")
row2.add(distanceToBallInStopModeConfig.lable)
distanceToBallInStopModeConfig.entry=Entry(row2,textvariable=distanceToBallInStopModeConfig.value)
row2.add(distanceToBallInStopModeConfig.entry)
# .....end config







variable = StringVar(robots)
variable.set("one") # default value




    
time=option()
gameMode=option()
gameMode.value = StringVar(refree)
gameMode.value.set("Halt") # default value
time.value = DoubleVar()
row1=PanedWindow(refree)
row1.pack(fill=BOTH,expand=0,side=TOP)
time.lable=Label(row1,text=" Time: ",font=("Tahoma",18),foreground="red")
row1.add(time.lable)
time.entry=Entry(row1,textvariable = time.value)
row1.add(time.entry)
gameMode.lable=Label(row1,text=" Game Mode: ",font=("Tahoma",18),foreground="red")
row1.add(gameMode.lable)
gameMode.optionmenu=OptionMenu(row1, gameMode.value, "Halt", "Stop", "Play")
row1.add(gameMode.optionmenu)


time.entry.insert(-1,0)


test2=PanedWindow(refree)
test2.pack(fill=BOTH,expand=0,side=TOP)
ali2=Label(test2,text="data",font=("Tahoma",18),foreground="red")
test2.add(ali2)
dataInDataBase2=Entry(test2)
test2.add(dataInDataBase2)


# idString = IntVar()
# nameString = StringVar()
# valueString = DoubleVar()  
# Label(config,text="Set Data",font=("Tahoma",18),foreground="red" ).grid(row=0,columnspan=6,pady=5,padx=5)
# Label(config,text="ID: ",font=("Tahoma",9),foreground="green").grid(row=1,column=0)
# id=Entry(config,textvariable=idString).grid(row=1,column=1)
# Label(config,text="name: ",font=("Tahoma",9),foreground="green").grid(row=1,column=2)
# name=Entry(config,textvariable=nameString).grid(row=1,column=3)
# Label(config,text="value: ",font=("Tahoma",9),foreground="green").grid(row=1,column=4)
# value=Entry(config,textvariable=valueString).grid(row=1,column=5)
# save = partial(save, idString,nameString, valueString)  
# setbtn=Button(config,text="set",bg="yellow",fg="red",command=save)
# setbtn.grid(row=2,columnspan=6,pady=5,padx=5)








frame = Frame(
            master=config,
            relief=RAISED,
            borderwidth=1
        )
#frame.grid(row=2, column=2, padx=5, pady=5)
#label = Label(master=frame, text="hello")
#label.pack()
refree.mainloop()
robots.mainloop()
config.mainloop()

print(data.findInSetData('sd'))
