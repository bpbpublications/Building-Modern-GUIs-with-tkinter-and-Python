from tkinter import * # importing module
from tkinter.ttk import Combobox

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('300x200')
myroot.title('Comboboxcreation')

myval = StringVar()

def mydisplay():
    myval = mycombo.get()
    print(myval)

# creating a list of values
myl1 = ['Hindi','English','Telugu','Bengali']
myval.set('English')
#combobox object creation
mycombo = Combobox(myroot, values = myl1 , height = 2, textvariable = myval ,postcommand = mydisplay) #  , height = 2 : only 2 items and default width is 20
mycombo.pack()

myroot.mainloop() # display window until we press the close button
