from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.geometry('200x200') # but can be resized to any pixel until we are using root.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.

mytk_btn1 = Button(myroot, text = 'Background color',font = ('Calibri',15),fg = 'Blue')
mytk_btn1.bind('<Enter>',lambda e: myroot.configure(background = 'LightBlue'))
mytk_btn1.bind('<Leave>',lambda e: myroot.configure(background = 'LightGreen'))
mytk_btn1.pack()

myroot.mainloop()
