from tkinter import *

myroot = Tk()

myl1_label = Label(myroot,text = 'Hey! I', bd = 2, relief = 'solid',font = ('Calibri',15))
myl1_label.pack()

myl2_label = Label(myroot,text = 'love', bd = 5, relief = 'sunken',font = ('Calibri',15), padx = 10,pady = 10)
myl2_label.pack(padx = 10, pady = 10)

myl3_label = Label(myroot,text = 'python', bd = 5, relief = 'raised',font = ('Calibri',15), padx = 10,pady = 10)
myl3_label.pack(padx = 10, pady = 10)

myl4_label = Label(myroot,text = 'to', bd = 5, relief = 'groove',font = ('Calibri',15), padx = 10,pady = 10)
myl4_label.pack(padx = 10, pady = 10)

myl5_label = Label(myroot,text = 'read', bd = 5, relief = 'groove',font = ('Calibri',15), padx = 10,pady = 10)
myl5_label.pack(padx = 10, pady = 10)

myroot.mainloop()
