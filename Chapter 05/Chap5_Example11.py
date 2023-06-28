from tkinter import *

class MyStringVar_key_text(Tk):
    def __init__(self):
        super().__init__()
        self.myval1 = StringVar()
        self.title('StringVar() and textvariable a tkinter label')
        self.myl2= Label(self,font = 'Helvetica',textvariable= self.myval1,relief = 'groove')
        self.myl2.pack()
        self.myl3= Label(self,font = ('Arial',12),text= 'Hello',relief = 'groove')
        self.myl3.pack(padx = 10, pady = 10)
        self.myl3['text'] = 'Key/value pair approach of setting text'
        self.myval1.set('using textvariable set')

if __name__ == "__main__":
    myroot = MyStringVar_key_text()
    myroot.geometry('400x100')
    myroot.mainloop()
