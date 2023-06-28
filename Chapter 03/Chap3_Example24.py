from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('200x200')

COLOR1 = 'LightGreen'
COLOR2 = 'LightBlue'

def mydisplay():
    if myi1.get() == 1:
        myroot.configure(bg = COLOR1)
    elif myi1.get() == 2:
        myroot.configure(bg = COLOR2)

myi1 = IntVar()
myr1 = Radiobutton(myroot, text = COLOR1, value = 1, variable = myi1)
myr1.pack()

myr2 = Radiobutton(myroot, text = COLOR2, value = 2, variable = myi1)
myr2.pack()

mybtn = Button(myroot, text = 'Background_Click', command = mydisplay)
mybtn.pack()

myroot.mainloop() # display window until we press the close button
