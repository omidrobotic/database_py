import data
from tkinter import *
from tkinter import messagebox
from functools import partial  


def save(id,name,value):
    data.clearSetData(id.get())
    print(name.get())
    data.setDataValue(id.get(),name.get(),value.get())
    messagebox.showinfo("success","saved!!!!")
gui = Tk()
gui.title("Omid Robotic User Interface")
gui.geometry('600x400')
gui.resizable(width=True,height=True)



idString = IntVar()
nameString = StringVar()
valueString = DoubleVar()  
Label(gui,text="Set Data",font=("Tahoma",18),foreground="red" ).grid(row=0,columnspan=6,pady=5,padx=5)
Label(gui,text="ID: ",font=("Tahoma",9),foreground="green").grid(row=1,column=0)
id=Entry(gui,textvariable=idString).grid(row=1,column=1)
Label(gui,text="name: ",font=("Tahoma",9),foreground="green").grid(row=1,column=2)
name=Entry(gui,textvariable=nameString).grid(row=1,column=3)
Label(gui,text="value: ",font=("Tahoma",9),foreground="green").grid(row=1,column=4)
value=Entry(gui,textvariable=valueString).grid(row=1,column=5)
save = partial(save, idString,nameString, valueString)  
setbtn=Button(text="set",bg="yellow",fg="red",command=save)
setbtn.grid(row=2,columnspan=6,pady=5,padx=5)








frame = Frame(
            master=gui,
            relief=RAISED,
            borderwidth=1
        )
#frame.grid(row=2, column=2, padx=5, pady=5)
#label = Label(master=frame, text="hello")
#label.pack()
gui.mainloop()
print(data.findInSetData('sd'))
