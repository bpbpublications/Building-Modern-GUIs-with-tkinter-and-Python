from tkinter import * 
myroot = Tk()
myroot.geometry('300x160+150+300')

myroot.update()
print(myroot.winfo_geometry())

myroot.mainloop()