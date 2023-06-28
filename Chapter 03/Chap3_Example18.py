from tkinter import *
from tkinter.ttk import *

myroot = Tk()
myroot.geometry('300x150')
myroot.title('CheckButton widget')

def myget():
    if i2.get() == 'check':
        s1.set('Checked')
    else:
        s1.set('UnChecked')
    

i2 = StringVar()
myc2 = Checkbutton(myroot, text = 'Check/Uncheck', variable = i2, offvalue = 'uncheck', onvalue = 'check', command = myget)
myc2.pack()

s1 = StringVar()
mye1 = Entry(myroot, font = ('Calibri',12), textvariable= s1)
mye1.pack(pady = 10)

myroot.mainloop()
