from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.geometry('200x200') # but can be resized to any pixel until we are using root.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.

myroot.bind('<Shift-Up>',lambda e: myroot.configure(background = 'LightBlue')) # on key pressing Shift-Up
myroot.bind('<Shift-Down>',lambda e: myroot.configure(background = 'LightGreen')) # on key pressing Shift-Down
myroot.bind('<Shift-Left>',lambda e: myroot.configure(background = 'LightPink')) # on key pressing Shift-Left
myroot.bind('<Shift-Right>',lambda e: myroot.configure(background = 'LightYellow')) # on key pressing Shift-Right

myroot.bind('<Alt-Up>',lambda e: myroot.configure(background = 'LightBlue')) # on key pressing Alt-Up
myroot.bind('<Alt-Down>',lambda e: myroot.configure(background = 'LightGreen')) # on key pressing Alt-Down
myroot.bind('<Alt-Left>',lambda e: myroot.configure(background = 'LightPink')) # on key pressing Alt-Left
myroot.bind('<Alt-Right>',lambda e: myroot.configure(background = 'LightYellow')) # on key pressing Alt-Right

myroot.bind('<Control-Up>',lambda e: myroot.configure(background = 'LightBlue')) # on key pressing Control-Up
myroot.bind('<Control-Down>',lambda e: myroot.configure(background = 'LightGreen')) # on key pressing Control-Down
myroot.bind('<Control-Left>',lambda e: myroot.configure(background = 'LightPink')) # on key pressing Control-Left
myroot.bind('<Control-Right>',lambda e: myroot.configure(background = 'LightYellow')) # on key pressing Control-Right

myroot.mainloop()
