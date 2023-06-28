from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('300x300')
myroot.title('rectanglecreation')

#canvas creation
myc1 = Canvas(myroot, width = 300, height = 300, bg = 'LightBlue')
myc1.pack()

# rectangle creation
myrect = myc1.create_rectangle(100,100,300,300, fill = 'Red', outline  = 'Blue')

myroot.mainloop() # display window until we press the close button
