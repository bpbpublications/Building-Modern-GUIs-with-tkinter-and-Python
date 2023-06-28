from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window
# we should first know how to create a window if want to perform graphics coding.
# but output window will not be displayed right now

myroot.geometry('200x200') # but can be resized to any pixel until we are using root.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.

mystr = StringVar() # S1
print(type(mystr)) # S2
my_entry = Entry(myroot, font = ('Calibri',12),textvariable = mystr)
my_entry.pack()

def myshow():
    mydata = mystr.get() # S3
    print(mydata)
    mystr.set('') # S4

my_btn = Button(myroot, font = ('Calibri',12), text = 'Get Data!',command = myshow)
my_btn.pack()

myroot.mainloop()
