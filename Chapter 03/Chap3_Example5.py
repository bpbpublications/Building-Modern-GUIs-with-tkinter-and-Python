from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.geometry('370x100') # but can be resized to any pixel until we are using myroot.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.
myroot.title('event handling through Cmd prompt')

def mydisplay():
    print("Clicked !!!")

mytk_button1 = Button(myroot, text = 'Login',font = ('Calibri',15),fg = 'Blue',command = mydisplay)
mytk_button1.pack()

myroot.mainloop()
