from tkinter import * # importing module
from tkinter.ttk import Combobox

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('300x200')
myroot.title('Comboboxcreation')

myl2 = Label(myroot, text = 'Choose your mother tongue')
myl2.pack(pady = 10)

def mydisplay(myevent):
    print(mycombo.get())

# creating a list of values
myl1 = ['Hindi','English','Telugu','Bengali']

#combobox object creation
mycombo = Combobox(myroot, values = myl1 , height = 2) #  , height = 2 : only 2 items and default width is 20
mycombo.pack(pady = 10)
mycombo.current(1)
mycombo.bind("<<ComboboxSelected>>", mydisplay)

myroot.mainloop() # display window until we press the close button
