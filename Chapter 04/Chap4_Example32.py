from tkinter import * # importing module
from tkinter.ttk import Combobox

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('300x200')
myroot.title('Comboboxcreation')

# creating a list of values
mylist1 = ['Apple','Litchi','Mango','Pomengranate']

# assigning font tuple
myfont = ("Times New Roman", 14, "italic")

#assigning label
myl1 = Label(myroot, text = 'Choose from your favorate fruit')
myl1.pack(pady = 10)

#combobox object creation
mycombo = Combobox(myroot, values = mylist1 , height = 2, font = myfont) #  , height = 2 : only 2 items and default width is 20
mycombo.pack(pady = 10)
mycombo.current(1)

# specifying font of the list box of Combobox
myroot.option_add('*TCombobox*Listbox.font', myfont)

myroot.mainloop() # display window until we press the close button
