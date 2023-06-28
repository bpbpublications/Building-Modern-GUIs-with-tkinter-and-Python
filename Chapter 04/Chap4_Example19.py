from tkinter import *

myroot = Tk()

# creating a float variable value holder
myv1 = DoubleVar()

#creation of horizontal slider
mys1 = Scale(myroot, from_=0, to=100, orient = 'horizontal', length = 200, width = 10,sliderlength = 50, label = 'MyScale Widget',troughcolor = 'Red', resolution = 10,tickinterval = 10)

# setting the scale value to 45
mys1.set(50)
mys1.pack()

myroot.title('MyScalewidget')
myroot.geometry("300x100+120+120")
myroot.mainloop()
