from tkinter import * 
myroot = Tk()
mycanvas = Canvas(myroot, width= 300 , height = 350)
print("Before packing width is: " + str(mycanvas.winfo_width()))
print("Before packing height is: " + str(mycanvas.winfo_height()))
mycanvas.pack()
mycanvas.update()
print("After packing and updating width is: " + str(mycanvas.winfo_width()))
print("After packing and updating height is: " + str(mycanvas.winfo_height()))

