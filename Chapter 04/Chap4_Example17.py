from tkinter import *

myroot = Tk()

# creating a float variable value holder
myv1 = DoubleVar()

#creation of horizontal slider
mys1 = Scale(myroot, from_=0, to=100, orient = HORIZONTAL, length = 200, width = 10,
           sliderlength = 50, label = 'myscale',
           variable = myv1) # default length = 100, width = 15, sliderlength = 30
# setting the scale value to 45
mys1.set(45)
mys1.pack()

def mydisplay():
    # will get the value
    print(myv1.get())
    # will return the coordinates corresponding to the given scale value
    print(mys1.coords(value = myv1.get()))

# creating a button widget
mybtn1 = Button(myroot, text = "GetValue", command = mydisplay, bg = 'LightBlue')
mybtn1.pack(pady = 10)

myroot.title('MyScalewidget')
myroot.geometry("300x200+120+120")
myroot.mainloop()
