from tkinter import *

myroot = Tk()

# creating a float variable value holder
myv1 = DoubleVar()

#creation of horizontal slider
mys1 = Scale(myroot, from_=0, to=100, orient = VERTICAL, length = 200, width = 10,
           sliderlength = 50, label = 'MyScale Widget',
           variable = myv1) # default length = 100, width = 15, sliderlength = 30
# setting the scale value to 35
mys1.set(35)
mys1.pack()

def mydisplay():
    # will display the value
    myl1.config(text = 'The scale value is: ' + str(myv1.get()), font = ('Verdana',12))

# creating a button widget
mybtn1 = Button(myroot, text = "GetValue", command = mydisplay, bg = 'LightBlue')
mybtn1.pack(pady = 10)

#creating a label widget
myl1 = Label(myroot)
myl1.pack(pady=10)

myroot.title('MyScalewidget')
myroot.geometry("300x300+120+120")
myroot.mainloop()
