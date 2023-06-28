from tkinter import*

myroot=Tk()
myroot.geometry("220x100")

myframe1=Frame(myroot)
myl1 = Label(myframe1, text = 'Name')
myl1.grid(row = 0, column = 0)
myl2 = Label(myframe1, text = 'Age')
myl2.grid(row = 1, column = 0)
myl3 = Label(myframe1, text = 'PhoneNumber')
myl3.grid(row = 2, column = 0)

mye1 = Entry(myframe1)
mye1.grid(row = 0, column = 1)
mye2 = Entry(myframe1)
mye2.grid(row = 1, column = 1)
mye3 = Entry(myframe1)
mye3.grid(row = 2, column = 1)

mybtn = Button(myframe1, text = 'View')
mybtn.grid(row = 3, columnspan  = 2)
myframe1.grid(row=0, column=0)

myroot.mainloop()
