from tkinter import *  
from tkinter import messagebox  
  
myroot = Tk()  
myroot.geometry("300x150")
myroot.title('AskQuestion')

def mydisplay():
    ans = messagebox.askquestion("AskQuestion example","Do you want to continue")  
    if ans == 'yes':
        messagebox.showinfo('Message','You have chosen Yes')
    else:
        messagebox.showinfo('Message','You have chosen No')

mybtn1 = Button(myroot, text = 'ClickAskMsg', command = mydisplay)
mybtn1.pack()
myroot.mainloop() 
