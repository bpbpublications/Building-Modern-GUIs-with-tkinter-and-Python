from tkinter import *

myroot = Tk()
myroot.geometry('250x100')
myroot.title('SpinBox')

# creation of spinbox
mys1 = Spinbox(font = ('Calibri',15),  from_ = 10, to = 20)
mys1.pack()

myroot.mainloop()
