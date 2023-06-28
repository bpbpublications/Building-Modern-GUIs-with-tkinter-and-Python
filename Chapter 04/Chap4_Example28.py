from tkinter import * # importing module
from tkinter.ttk import Combobox

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('300x200')
myroot.title('Comboboxcreation')

# creating a list of values
myl2 = list(range(1,25))

#combobox object creation
mycombo = Combobox(myroot, values = myl2 , width = 15) #  , height = 2 : only 2 items
mycombo.pack(padx = 50, pady = 10)

myroot.mainloop() # display window until we press the close button
