from tkinter import *
myroot = Tk()
myroot.geometry('300x300')
def myselected():
    mychk1.config(state=NORMAL)

def mydisabled():
    mychk1.config(state=DISABLED)

mybtn1 = Button(myroot, text = 'Normal', command = myselected)
mybtn1.place(x = 50, y = 50)
mybtn2 = Button(myroot, text = 'Disabled', command = mydisabled)
mybtn2.place(x = 50, y = 100)

mychk1 = Checkbutton(myroot, text = 'CheckButton')
mychk1.place(x = 100, y = 150)

myroot.mainloop()
