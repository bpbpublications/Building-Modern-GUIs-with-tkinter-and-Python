from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.geometry('200x200') # but can be resized to any pixel until we are using root.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.

mybutton1 = Button(myroot, text = 'Click Me!!!', font = ('Arial',12))
mybutton1.bind('<Button>',lambda e: myroot.configure(background = 'LightBlue')) # on Mouse pressing Button
mybutton1.bind('<ButtonRelease>',lambda e: myroot.configure(background = 'Red')) # on Mouse releasing Button
mybutton1.pack()

myroot.mainloop()
