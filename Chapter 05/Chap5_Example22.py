from tkinter import *  
from tkinter import messagebox  
  
myroot = Tk()  
myroot.geometry("300x150")
myroot.title('AskRetryCancel')

def mydisplay():
    messagebox.askretrycancel("AskRetryCancel example","Will you do it")  

mybtn1 = Button(myroot, text = 'ClickRetryCancelMsg', command = mydisplay)
mybtn1.pack()
myroot.mainloop()  
