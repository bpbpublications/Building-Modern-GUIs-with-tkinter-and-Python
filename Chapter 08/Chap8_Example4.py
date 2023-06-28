from tkinter import *

myroot = Tk()
mymenu_bar = Menu(myroot)

def myselected(menu):
    menu.entryconfig(1, label="Selected!")

myedit_menu = Menu(mymenu_bar, tearoff=0)
myedit_menu.add_command(label="Demo1", command=lambda: myselected(myedit_menu))
mymenu_bar.add_cascade(label="Edit", menu=myedit_menu)

myroot.config(menu=mymenu_bar)
myroot.mainloop()
