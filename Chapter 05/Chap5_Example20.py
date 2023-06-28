from tkinter import *  
from tkinter import messagebox  
  
myroot = Tk()  
myroot.geometry("300x150")
myroot.title('AskOkCancel')

def mydisplay():
    messagebox.askokcancel("AskOkCancel example","Redirecting to www.abc.com")  

mybtn1 = Button(myroot, text = 'ClickOkCancelMsg', command = mydisplay)
mybtn1.pack()
myroot.mainloop()  
