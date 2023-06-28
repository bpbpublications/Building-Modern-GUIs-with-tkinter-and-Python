from tkinter import *
myroot = Tk()
myroot.geometry('300x250')
def myselected():
    mychk1.select()

def mydeselect():
    mychk1.deselect()

def mytoggle():
    mychk1.toggle()

def myinvoke():
    myl1 = Label(myroot, text = 'CheckStat')
    myl1.place(x = 20, y = 150)
 
mybtn1 = Button(myroot, text = 'Select', command = myselected)
mybtn1.place(x = 50, y = 50)
mybtn2 = Button(myroot, text = 'Deselect', command = mydeselect)
mybtn2.place(x = 50, y = 100)
mybtn3 = Button(myroot, text = 'Toggle', command = mytoggle)
mybtn3.place(x = 150, y = 50)
mybtn4 = Button(myroot, text = 'Invoke', command = myinvoke) # will call the command associated with the button initially on run
mybtn4.place(x = 150, y = 100)
mybtn4.invoke()

mychk1 = Checkbutton(myroot, text = 'CheckButton')
mychk1.place(x = 100, y = 150)

myroot.mainloop()
