from tkinter import *  
from tkinter import messagebox  
  
myroot = Tk()  
myroot.geometry("300x150")
myroot.title('AskYesNo')

def mydisplay():
    messagebox.askyesno("AskYesNo example","Will you do it")  

mybtn1 = Button(myroot, text = 'ClickYesNoMsg', command = mydisplay)
mybtn1.pack()
myroot.mainloop()  
