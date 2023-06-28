from tkinter import *

myroot = Tk() # creating an object of Tk class -- object of window

myroot.geometry('200x200') # but can be resized to any pixel until we are using root.resizeable
myroot.resizable(0,0) # window size is fixed. cannot be larger or smaller.

num = 1
def mydisplay(e):
    global num
    num = num + 1
    if num%2 == 0:
        myroot.configure(background = 'LightBlue')
    else:
        myroot.configure(background = 'Red')
        
mybutton1 = Button(myroot, text = 'Click Me!!!', font = ('Arial',12))
mybutton1.bind('<Button>',mydisplay) # on Mouse pressing Button
mybutton1.bind('<ButtonRelease>',mydisplay) # on Mouse releasing Button
mybutton1.pack()

myroot.mainloop()
