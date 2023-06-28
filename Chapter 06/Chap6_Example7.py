from tkinter import *

#main window creation
myroot = Tk()

#window size
myroot.geometry('300x300')

# 1st paned window object
mypw1 = PanedWindow(myroot)

#expand option for widgets to expand and fill for letting widgets adjust itself
mypw1.pack(fill = BOTH, expand = 1)  

# entry widget creation
mye1 = Entry(mypw1, bd =  5, relief = 'groove', font = ('Calibri',12), bg = 'LightBlue')  

# will add entry widget to the panedwindow
mypw1.add(mye1)

# 2nd paned window object
mypw2 = PanedWindow(mypw1, orient = VERTICAL) 

#adding 2nd paned window to the 1st paned window
mypw1.add(mypw2)  

# spinbox object creation
mye2 = Spinbox(mypw2, from_ = 10, to = 20, font = ('Calibri',12), bg = 'LightPink')  

# another entry widget creation
mye3 = Entry(mypw2, bg = 'LightGreen',font = ('Calibri',12) )

#setting the value to 3
mye3.insert(0,3)

# to show sash 
mypw1.configure(sashrelief = RAISED)

# subtract function
def subtract():
    num1 = int(mye2.get()) # getting value of spinbox
    num2 = int(mye3.get()) # getting value of entry
    mydata = str(num1-num2)  
    mye1.insert(1,mydata)  

# adding spinbox to the 2nd paned window
mypw2.add(mye2)

# adding entry to the 2nd paned window
mypw2.add(mye3)

# creation of button widget
mybtn = Button(mypw2, text = "Subtract", command = subtract)  

# adding button to the 2nd paned window
mypw2.add(mybtn)  

# infinte loop
myroot.mainloop()
