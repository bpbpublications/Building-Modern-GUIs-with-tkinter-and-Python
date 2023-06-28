from tkinter import *  
from tkinter import messagebox  
  
myroot = Tk()  
myroot.geometry("300x150")
myroot.title('Showinfo example')

def mydisplay():
    messagebox.showinfo("Showinfoexample","This is a basic showinfo example")  

mybtn1 = Button(myroot, text = 'ClickShowInfo', command = mydisplay)
mybtn1.pack()
myroot.mainloop()  
