from tkinter import *

myroot = Tk()

myb1 = Button(myroot, text = 'Without highlight thickness')
myb1.grid(row = 0, column = 1)

myb2 = Button(myroot, text = 'With highlight thickness',
                      highlightthickness=10,
                      )
myb2.grid(row = 1, column = 1, padx = 10, pady = 10)

myroot.mainloop()
