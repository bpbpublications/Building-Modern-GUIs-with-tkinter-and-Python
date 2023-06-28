from  tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
myroot = Tk()
myroot.title('AskSaveasFileName')
myroot.geometry('350x150')
def saveas():
    mytxt = mye1.get()
    myfiles = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    myfile1 = asksaveasfilename(filetypes = myfiles, defaultextension = myfiles, confirmoverwrite = False)
    fname = myfile1
    if fname != '':
        try:
            myfile1 = open(fname, "a+")
            myfile1.write('\n' +str(mytxt))
            myfile1.close() 
            messagebox.showinfo('Data Writing!', 'Data has been appended')
        except:
            print('There is no such file')

mye1 = Entry(myroot, font=('Verdana',12))
mye1.place(x=10,y=10,width=200,height=100)
mybtn1 = Button(myroot,text='SaveasFileName',font=('Courier',10), width=14,bd=10, command =saveas)
mybtn1.place(x=210,y=110)

myroot.mainloop()
