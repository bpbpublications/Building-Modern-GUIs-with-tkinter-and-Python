from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.maxsize(300,300) # maximum size of window- It can be smaller like anything byt maximum up to 300 only
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.
mytk_label = Label(myroot,text = 'Python\nis\nawesome', font = ('Calibri',15),bg = 'Yellow',fg = 'Black',
                   width = '15', height = '3')
mytk_label.pack()

myroot.mainloop()
