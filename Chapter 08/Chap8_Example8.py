from tkinter import *  

myroot = Tk()  
myroot.geometry("300x150")  

# creating menubutton
menubutton = Menubutton(myroot, text = "My Hobby", relief = FLAT)  
menubutton.grid()

# creating pull down menu
menubutton.menu = Menu(menubutton, tearoff = 0)  
menubutton["menu"]=menubutton.menu

# creating radiobutton when clicked the color will be changed to green
myval1 = IntVar()
menubutton.menu.add_radiobutton(label = "Reading Books", value = 1, variable=myval1, selectcolor = 'green')  
menubutton.menu.add_radiobutton(label = "Playing Outdoor games", value = 2, variable = myval1, selectcolor = 'green')  
menubutton.pack()  

myroot.mainloop() 
