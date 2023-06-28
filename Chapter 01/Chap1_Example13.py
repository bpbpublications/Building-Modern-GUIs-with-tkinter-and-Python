from tkinter import *

myroot = Tk()
str1 = StringVar()
mye1 = Entry(myroot,selectbackground= 'Green',selectforeground= 'Red',  textvariable = str1)
mye1.pack()
str1.set('python')

myroot.mainloop()
