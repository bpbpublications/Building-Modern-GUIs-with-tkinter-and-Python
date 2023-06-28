from tkinter import *

myroot = Tk()
mymenu_bar = Menu(myroot)

myedit_menu = Menu(mymenu_bar, tearoff=0)  # L2
myedit_menu.add_command(label="Cut")
myedit_menu.add("command", label="Copy", command=lambda: print("Copy"))
myedit_menu.add("command", label="Paste", command=lambda: print("Paste")) # using 
myedit_menu.add(itemType = "command", label="Exit", command=lambda: myroot.quit()) # using itemType
mymenu_bar.add_cascade(label="Edit", menu=myedit_menu)

myroot.config(menu=mymenu_bar)
myroot.mainloop()
