from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('360x360')
myroot.title('ImageCanvas')

myc1 = Canvas(myroot, width = 360, height = 360, bg = 'LightBlue')
myc1.pack()

myphoto = PhotoImage(file = 'butterfly1.gif')
myc1.create_image(0,0,image = myphoto, anchor = NW)

myroot.mainloop() # display window until we press the close button
