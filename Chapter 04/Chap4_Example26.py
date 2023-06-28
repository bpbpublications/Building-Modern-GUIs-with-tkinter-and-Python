from tkinter import *

myroot=Tk()

def myclick():
    mytext.insert('insert',"<>")
    mytext.mark_names() # all the mark names are returned
    mytext.mark_set('insert',END) # a new position is informed of the given mark
    mytext.mark_gravity('insert',RIGHT) # changing the gravity of mark to right
mybtn1=Button(myroot,text="Myclick",command=myclick)
mybtn1.pack()

mytext=Text(myroot , width = 55, height = 10)
mytext.pack()

myroot.mainloop()
