from tkinter import *

myroot = Tk()
myroot.geometry('200x200')
myroot.resizable(0,0)

myint = DoubleVar()
myint1 = DoubleVar()
myint2 = DoubleVar()

my_entry = Entry(myroot, font = ('Calibri',12),textvariable = myint)
my_entry.pack()

my_entry1 = Entry(myroot, font = ('Calibri',12),textvariable = myint1)
my_entry1.pack()

def mydisplay():
    mydata1 = myint.get()
    mydata2 = myint1.get()
    mydata3 = mydata1 - mydata2
    myint2.set(mydata3)

my_btn = Button(myroot, font = ('Calibri',12), text = 'Difference',command = mydisplay)
my_btn.pack()
my_entry2 = Entry(myroot, font = ('Calibri',12),textvariable = myint2)
my_entry2.pack()
my_entry2.configure(state = 'readonly')

myroot.mainloop()

