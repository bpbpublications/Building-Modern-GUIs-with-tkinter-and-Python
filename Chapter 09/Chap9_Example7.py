from tkinter import *
from tkinter.colorchooser import *

def myclickme():
    (my_rgb, mycolor) = askcolor(title = 'Please choose your color') # tuple will be returned
    print(my_rgb)
    print(mycolor)
    myroot.configure(background=mycolor)
    
myroot = Tk()
myroot.title('ColorPicker')
mybtn1 = Button(myroot, text="Choose Color",command=myclickme)
mybtn1.pack()

myroot.geometry("300x300")
myroot.mainloop()
