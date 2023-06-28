from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('300x200')
myroot.title('Textwriting')

# canvas object creation
myc1 = Canvas(myroot, width = 300, height = 200, bg = 'LightBlue')
# create text
myc1.create_text(10, 100, anchor=W, font="Helvetica",
            text="Hey! I am writing text in Canvas")
myc1.pack()

myroot.mainloop() # display window until we press the close button
