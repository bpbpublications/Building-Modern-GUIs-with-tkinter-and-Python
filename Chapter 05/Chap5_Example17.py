from tkinter import *  
from tkinter import messagebox  
  
myroot = Tk()  
myroot.geometry("300x150")
myroot.title('Warningmessage')

def mydisplay():
    messagebox.showwarning("ShowWarningexample","This is a basic warning message example")  

mybtn1 = Button(myroot, text = 'ClickWarningMsg', command = mydisplay)
mybtn1.pack()
myroot.mainloop() 
