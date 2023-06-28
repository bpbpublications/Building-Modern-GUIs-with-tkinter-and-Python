from tkinter import *

myroot=Tk()

def myclick():
    mytext.insert('insert',"<>")

mybtn1=Button(myroot,text="Myclick",command=myclick)
mybtn1.pack()

mytext=Text(myroot, width = 55, height = 25)
mytext.pack()

def insertimage():
    mytext.image_create('insert',image = myimage1)

myimage1 = PhotoImage(file = 'butterfly1.gif')
mybtn2=Button(myroot,text="CreateImage",command = insertimage)
mybtn2.pack(pady = 10)

myroot.mainloop()

