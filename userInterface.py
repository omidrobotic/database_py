import data
from tkinter import *
window = Tk()
window.title("Omid Robotic User Interface")
window.geometry('600x400')
window.resizable(width=True,height=True)
Label(window,text="Set Data",font=("Tahoma",18),foreground="red" ).pack()

window.mainloop()
print(data.findInSetData('ali'))
