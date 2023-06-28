from tkinter import *

myroot = Tk()
myroot.geometry('300x300')

# stringvar variable
a1 = StringVar()

# mydisplay function
def mydisplay():
    myroot.configure(bg = a1.get())

# creation of spinbox
mys1 = Spinbox(font = ('Calibri',15), command = mydisplay, values = ['Red','Green','Blue','Violet','Indigo','Magenta','Yellow'], textvariable = a1)
mys1.pack()

myroot.mainloop()
