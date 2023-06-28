from tkinter import *

myroot = Tk()

mytxt = 'Stay Safe from Corona Virus. Follow social distancing Please.:)'

# creation of message widget object
mymsg1 = Message( myroot, text=mytxt, relief=RAISED, font = ('Calibri',12), fg = 'Red', bg = 'LightGreen')

mymsg1.pack()
myroot.mainloop()
