from tkinter import *

class MySTATE:
    def __init__(self, myroot):
        self.myvar = StringVar()
        self.myvar.set('python')
        
        self.myl1 = Label(myroot, text = 'Normal state')
        self.myl1.grid(row = 0, column = 0)
        
        self.myl2 = Label(myroot, text = 'Disabled state')
        self.myl2.grid(row = 1, column = 0, pady = 10)
        
        self.myl3 = Label(myroot, text = 'Readonly state')
        self.myl3.grid(row = 2, column = 0, pady = 10)
        
        self.mye1 = Entry(myroot, textvariable=self.myvar, width=15, state = 'normal')
        self.mye1.grid(row = 0, column = 1, padx = 10)
        self.mye2 = Entry(myroot, textvariable=self.myvar, width=15, state = 'disabled')
        self.mye2.grid(row = 1, column = 1, padx = 10)
        self.mye3 = Entry(myroot, textvariable=self.myvar, width=15, state = 'readonly')
        self.mye3.grid(row = 2, column = 1, padx = 10)

if __name__ == "__main__":
    myroot = Tk()
    myobj = MySTATE(myroot)
    myroot.mainloop()
