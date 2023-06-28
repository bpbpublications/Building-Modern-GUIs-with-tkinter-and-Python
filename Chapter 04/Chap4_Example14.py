from tkinter import *

myroot = Tk()
myroot.geometry('250x100')
myroot.title('SpinBox')

# creation of spinbox
mys1 = Spinbox(font = ('Calibri',15),  values = (10,35,49,40),  bd = 10,
relief = RAISED)
mys1.pack(pady = 10)

myroot.mainloop()
