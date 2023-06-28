from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.geometry('200x200') # but can be resized to any pixel until we are using root.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.

#using lambda expression
myshow1 = lambda e: myroot.configure(background = 'LightBlue')
myshow2 = lambda e: myroot.configure(background = 'LightGreen')
myshow3 = lambda e:  myroot.configure(background = 'LightPink')

mytk_btn1 = Button(myroot, text = 'Background color',font = ('Calibri',15),fg = 'Blue')
mytk_btn1.bind('<Button-1>',myshow1) # Left Key of mouse
mytk_btn1.bind('<Button-2>',myshow2) # Wheel Key of mouse
mytk_btn1.bind('<Button-3>',myshow3) # Right Key of mouse
mytk_btn1.pack()

myroot.mainloop()
