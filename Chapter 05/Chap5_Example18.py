from tkinter import *  
from tkinter import messagebox  
  
myroot = Tk()  
myroot.geometry("300x150")
myroot.title('Errormessage')

def mydisplay():
    messagebox.showerror("Showerrorexample","This is a basic error message example")  

mybtn1 = Button(myroot, text = 'ClickErrorMsg', command = mydisplay)
mybtn1.pack()
myroot.mainloop()  
