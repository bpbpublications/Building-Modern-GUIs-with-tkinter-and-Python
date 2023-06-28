from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('300x300')
myroot.title('arccreation')

# canvas widget creation
myc1 = Canvas(myroot, width = 300, height = 300, bg = 'LightBlue')
myc1.pack()

# arc creations
myc1.create_arc(50,50,150,150)
myc1.create_arc(120,120,200,200, extent = 120)

#fill: arc interior filled with Red color
myc1.create_arc(180,180,250,250, extent = 120, style = CHORD, fill = 'Red')

# start angle par: start location in degrees whose default is 0 deg
# extent angle par: from the start location the no. of degrees to extend the arc whose default is 90 deg
# style par: arc style to draw could be pieslice(default), chord and arc
myc1.create_arc(180,250,270,270, start = 50, extent = 120, style = ARC)

myroot.mainloop() # display window until we press the close button
