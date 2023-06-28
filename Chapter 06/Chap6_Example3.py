from tkinter import*

myroot=Tk()
myroot.geometry("430x100")

# myframe1 with row = 0, column = 0
myframe1=Frame(myroot)
myframe1.grid(row=0, column=0)

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

# mysideframe1 with row = 0, column = 1
mysideframe1=Frame(myroot)
mysideframe1.grid(row=0, column=1, padx = 20)

myl1 = Label(mysideframe1, text = 'Sex')
myl1.grid(row = 0, column = 0)
myl2 = Label(mysideframe1, text = 'City')
myl2.grid(row = 1, column = 0)
myl3 = Label(mysideframe1, text = 'Address')
myl3.grid(row = 2, column = 0)

mye1 = Entry(mysideframe1)
mye1.grid(row = 0, column = 1)
mye2 = Entry(mysideframe1)
mye2.grid(row = 1, column = 1)
mye3 = Entry(mysideframe1)
mye3.grid(row = 2, column = 1)

mybtn = Button(mysideframe1, text = 'Display')
mybtn.grid(row = 3, columnspan  = 2)

myroot.mainloop()
