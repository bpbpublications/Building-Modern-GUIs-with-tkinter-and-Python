from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.geometry('200x200') # but can be resized to any pixel until we are using root.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.

myroot.bind('1',lambda e: myroot.configure(background = 'LightBlue')) # on key pressing 1 in laptop
myroot.bind('2',lambda e: myroot.configure(background = 'LightGreen')) # on key pressing 2 in laptop
myroot.bind('3',lambda e: myroot.configure(background = 'LightPink')) # on key pressing 3 in laptop

myroot.mainloop()
