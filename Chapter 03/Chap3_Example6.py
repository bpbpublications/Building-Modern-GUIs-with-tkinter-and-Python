from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.geometry('300x300') # but can be resized to any pixel until we are using root.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.

def myshow1():
    myroot.configure(background = 'LightBlue')

mytk_button1 = Button(myroot, text = 'Change Background color',font = ('Calibri',15),fg = 'Blue')
mytk_button1.config(command = myshow1)
mytk_button1.pack()

myroot.mainloop()
