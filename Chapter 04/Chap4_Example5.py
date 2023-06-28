from tkinter import *

class MyIndex_Select_adjust(Tk):
     def __init__(self):
        super().__init__()
        self.title('MyIndex and Select_adjust Example')
        self.mye1= Entry(self,font = ('Arial',12),width = 20, bd = 5)
        self.mye1.pack(side = LEFT)
        self.mye1.focus()
        self.mye1.insert(0,'Demonstration')
        self.mye1.icursor(0)
       
        self.button1 = Button(self, text="Index", command=lambda: myindex(self,self.mye1))
        self.button1.pack(pady = 12)
        
        self.mybtn2 = Button(self, text="select_adjust", command=lambda: myselect_adjust(self,self.mye1))
        self.mybtn2.pack(pady = 10)
        
        def myindex(self, myentry):
            myentry.icursor(self.mye1.index(6))
        
        def myselect_adjust(self, myentry):
            myentry.select_adjust(5)

if __name__ == "__main__":
    myroot = MyIndex_Select_adjust()
    myroot.geometry('400x100')
    myroot.mainloop()
