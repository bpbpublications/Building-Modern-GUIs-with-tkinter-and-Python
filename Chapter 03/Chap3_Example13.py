from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.geometry('200x200') # but can be resized to any pixel until we are using root.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.

myroot.bind('<F1>',lambda e: myroot.configure(background = 'LightBlue')) # on key pressing Fn+F1 in laptop
myroot.bind('<F2>',lambda e: myroot.configure(background = 'LightGreen')) # on key pressing Fn+F2 in laptop
myroot.bind('<F3>',lambda e: myroot.configure(background = 'LightPink')) # on key pressing Fn+F3 in laptop
myroot.bind('<Delete>',lambda e: myroot.configure(background = 'LightYellow')) # on key pressing Delete

myroot.mainloop()
