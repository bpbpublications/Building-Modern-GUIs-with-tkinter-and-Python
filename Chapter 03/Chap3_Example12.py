from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.geometry('200x200') # but can be resized to any pixel until we are using root.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.

myroot.bind('<Key-a>',lambda e: myroot.configure(background = 'LightBlue')) # on pressing key 'a'
myroot.bind('<Key-b>',lambda e: myroot.configure(background = 'LightGreen')) # on pressing key 'b'
myroot.bind('<Key-c>',lambda e: myroot.configure(background = 'LightPink')) # on pressing key 'c'

myroot.mainloop()
