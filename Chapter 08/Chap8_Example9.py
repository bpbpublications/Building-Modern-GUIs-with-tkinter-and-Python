from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('400x400')
myroot.title('Linecreation')

# creation of canvas widget . draing a rectabgular area
myc1 = Canvas(myroot, width = 350, height = 350, bg = 'LightBlue') # L1
myc1.pack()

# drawing 2 lines
myline = myc1.create_line(0,0,300,150) # L2 (x1,y1,x2,y2)
mygreen_line = myc1.create_line(300,150,0,300, fill = 'Green') # L3(x1,y1,x2,y2)

myroot.mainloop() # display window until we press the close button
