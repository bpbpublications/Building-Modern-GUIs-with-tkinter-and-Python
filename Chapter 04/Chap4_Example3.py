from tkinter import *

class MydeleteExample(Tk):
     def __init__(self):
        super().__init__()
        self.title('MyDelete Example')
        self.mye1= Entry(self,font = ('Arial',12),width = 30, bd = 5)
        self.mye1.pack(side = LEFT)
                
        self.button1 = Button(self, text="Delete the text", command=lambda: mydelete(self,self.mye1))
        self.button1.pack(pady = 32)
        
        def mydelete(self, myentry):
            myentry.delete(first=0,last=15)

if __name__ == "__main__":
    myroot = MydeleteExample()
    myroot.geometry('400x100')
    myroot.mainloop()
