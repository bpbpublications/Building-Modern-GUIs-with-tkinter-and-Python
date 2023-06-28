from tkinter import*

myroot=Tk()
myroot.geometry("300x300")

myframe1=Frame(myroot, width=150, height=150, bg="Red")
myframe1.grid(row=0, column=0)

myframe2=Frame(myroot, width=150, height=150, bg="Green")
myframe2.grid(row=1, column=0)

myframe3=Frame(myroot, width=150, height=150, bg="Blue")
myframe3.grid(row=0, column=1)

myframe4=Frame(myroot, width=150, height=150, bg="Cyan")
myframe4.grid(row=1, column=1)

myroot.mainloop()
