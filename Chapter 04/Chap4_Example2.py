from tkinter import *

class MyLogin:
    def __init__(self, myroot):

        self.myl1 = Label(myroot, text = 'Username')
        self.myl1.grid(row = 0, column = 0)
        
        self.myl2 = Label(myroot, text = 'Password')
        self.myl2.grid(row = 1, column = 0, pady = 10)

        self.mye1 = Entry(myroot, width=15,  selectborderwidth = 3)
        self.mye1.grid(row = 0, column = 1, padx = 10)
        self.mye2 = Entry(myroot, width=15,show= '*')
        self.mye2.grid(row = 1, column = 1, padx = 10)
        
        def mydisplay():
            print("The username is: " + self.mye1.get())
            print("The password is: " +self.mye2.get())
        
        self.mybtn = Button(myroot, text = 'Login', command = mydisplay, font = ('Calibri',12))
        self.mybtn.grid(row = 2, columnspan = 3)

if __name__ == "__main__":
    myroot = Tk()
    myobj = MyLogin(myroot)
    myroot.title('Login Page')
    myroot.geometry('200x120')
    myroot.mainloop()
