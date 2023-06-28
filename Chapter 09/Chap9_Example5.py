from  tkinter import *
from tkinter.filedialog import asksaveasfile
myroot = Tk()
myroot.title('AskSaveasFile')
myroot.geometry('350x150')
def saveas():
    mytxt = mye1.get()
    myfiles = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    myfile1 = asksaveasfile(filetypes = myfiles, defaultextension = myfiles)
    myfile1.write(mytxt)

mye1 = Entry(myroot, font=('Verdana',12))
mye1.place(x=10,y=10,width=200,height=100)
mybtn1 = Button(myroot,text='SaveasFile',font=('Courier',10), width=10,bd=10, command =saveas)
mybtn1.place(x=220,y=110)

myroot.mainloop()
