from tkinter import *

class MyStringVartext(Tk):
    def __init__(self):
        super().__init__()
        self.myval1 = StringVar()
        self.title('StringVar() and textvariable a tkinter label')
        self.myl2= Label(self,font = 'Helvetica',textvariable= self.myval1,relief = 'groove')
        self.myl2.pack()
        self.myval1.set('python is awesome')

if __name__ == "__main__":
    myroot = MyStringVartext()
    myroot.geometry('400x130')
    myroot.mainloop()
