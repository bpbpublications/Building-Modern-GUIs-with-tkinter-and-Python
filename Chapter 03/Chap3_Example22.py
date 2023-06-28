from tkinter import *

myroot = Tk()
myroot.geometry('300x150')
myroot.title('CheckButton widget')

mynum1 = IntVar()
mynum2 = IntVar()
mys1 = StringVar()

def mydatainsertion():
    
    if mynum1.get() == 1 and mynum2.get() == 0:# reading status of checkbutton
        mys1.set("Python")# setting the value to the Entry widget
    
    if mynum1.get() == 0 and mynum2.get() == 1:
        mys1.set("C#.Net")
    
    if mynum1.get() == 1 and mynum2.get() == 1:
        mys1.set("I love to study both")
    
    if mynum1.get() == 0 and mynum2.get() == 0:
        mys1.set("I hate to study both")
     
myc1 =  Checkbutton(myroot, variable = mynum1, font = ('Calibri',12), text = 'Python', command = mydatainsertion)
myc1.pack()

myc2 =  Checkbutton(myroot,variable = mynum2, font = ('Calibri',12), text = 'C#.Net', command = mydatainsertion)
myc2.pack()

mye1 = Entry(myroot, font = ('Calibri',15), textvariable = mys1)
mye1.pack()

myroot.mainloop()
