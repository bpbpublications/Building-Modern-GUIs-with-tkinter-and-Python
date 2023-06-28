from tkinter import * # importing module
from tkinter.font import Font
myroot = Tk() # window creation and initialize the interpreter

myfont1 = Font(family = 'Calibri',size=12, weight = 'bold', slant='italic', underline = 1, overstrike = 1) # 1 means we require underline
myl1 = Label(myroot, text = 'Python', font = myfont1)
myl1.pack() # for displaying the label

myroot.mainloop() # display window until we press the close button
