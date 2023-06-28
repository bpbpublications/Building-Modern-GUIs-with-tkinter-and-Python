from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('350x350')
myroot.title('circlecreation')

# canvas object creation
myc1 = Canvas(myroot, width = 350, height = 350, bg = 'LightBlue')
myc1.pack()

# rectangle object creation
myrect = myc1.create_rectangle(100,100,350,350, fill = 'Red', outline  = 'Red')

#oval object creation
myc1.create_oval(100,100,350,350, fill = 'Yellow', outline  = 'Yellow')

myroot.mainloop() # display window until we press the close button
