from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter

#creating variables
mytxt_color = StringVar(myroot)
mytxt_color.set("black")

myshow = IntVar(myroot)

# creating main menu
mymenuBar = Menu(myroot)

mymenu1 = Menu(myroot) # L1

# creating submenu
mysubmenu = Menu(myroot)
mysubmenu.add_radiobutton(label="Radio 1", variable=mytxt_color, value="black", selectcolor = 'Red')
mysubmenu.add_radiobutton(label="Radio 2", variable=mytxt_color, value="green", selectcolor = 'Red')

mysubmenu1 = Menu(myroot)
mysubmenu1.add_checkbutton(label="Check 1", variable=myshow, selectcolor = 'Green')

mymenuBar.add_cascade(label="MyMenu", menu=mymenu1)
mymenu1.add_cascade(label="Submenu with Radio buttons", menu=mysubmenu)
mymenu1.add_separator()
mymenu1.add_cascade(label="Submenu with Check buttons", menu=mysubmenu1)

myroot.config(menu=mymenuBar) # display the menu to the window

myroot.mainloop()
