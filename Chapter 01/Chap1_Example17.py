from tkinter import *

myroot = Tk()
myroot.geometry('200x200')
myl1 = Label(myroot, text = 'Python',anchor = N, font = ("Calibri", "18", "bold italic underline"), 
             bd = 1, relief = 'sunken', width = 10,height = 5 )
myl1.pack()
myroot.mainloop()
