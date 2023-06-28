from tkinter import *  

myroot = Tk()  
myroot.geometry("300x150")  

# creating menubutton
menubutton = Menubutton(myroot, text = "My Hobby", relief = FLAT)  
menubutton.grid()

# creating pull down menu
menubutton.menu = Menu(menubutton, tearoff = 0)  
menubutton["menu"]=menubutton.menu

# creating checkbutton
menubutton.menu.add_checkbutton(label = "Reading Books", variable=IntVar())  
menubutton.menu.add_checkbutton(label = "Playing Outdoor games", variable = IntVar())  
menubutton.pack()  

myroot.mainloop()  
