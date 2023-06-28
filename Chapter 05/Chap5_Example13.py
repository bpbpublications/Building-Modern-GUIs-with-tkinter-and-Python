from tkinter import *

myroot = Tk()
mystr = StringVar()

# creation of message widget object
mymsg1 = Message( myroot, textvariable=mystr, relief=RAISED, font = ('Calibri',12), fg = 'Red', bg = 'LightGreen' )

mystr.set("This is a string message")
mymsg1.pack()
myroot.mainloop()
