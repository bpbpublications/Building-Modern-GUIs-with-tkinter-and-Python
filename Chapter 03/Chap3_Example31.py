from tkinter import *

myroot = Tk()

myroot.title("Fruit Selection")
myroot.geometry('300x150')

# List is created 
myoptions = ['Litchi', "Mango", "Apple", "Banana"]

# Tkinter variable is created 
myvar = StringVar(myroot)
myvar.set(myoptions[0])

# Create an option menu by passing the variable and option list
myselection = OptionMenu(myroot, myvar, *myoptions) # variable bound to option menu
myselection.pack()

# Create button with command
def mydisplay():
    print("The chosen value :", myvar.get())

mybtn_show = Button(myroot, text="Myshow", command=mydisplay)
mybtn_show.pack(pady = 30, side = LEFT, anchor = N)

myroot.mainloop()
