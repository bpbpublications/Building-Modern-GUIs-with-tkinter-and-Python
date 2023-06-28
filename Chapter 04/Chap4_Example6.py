from tkinter import *

class MySelectMethods(Tk):
     def __init__(self):
        super().__init__()
        self.title('MyIndex and Select_adjust Example')
        self.mye1= Entry(self,font = ('Arial',12),width = 20, bd = 5)
        self.mye1.pack(side = LEFT)
        self.mye1.focus()
        self.mye1.insert(0,'Demonstration')
        self.mye1.icursor(0)
        self.mye1.select_clear()
       
        self.button1 = Button(self, text="select_to", command=lambda: myselect_to(self,self.mye1))
        self.button1.pack(pady = 5)
        
        self.mybtn2 = Button(self, text="select_from", command=lambda: myselect_from(self,self.mye1))
        self.mybtn2.pack(pady = 5)
        
        self.mybtn3 = Button(self, text="select_range", command=lambda: myselect_range(self,self.mye1))
        self.mybtn3.pack(pady = 5)
        
        self.mybtn4 = Button(self, text="select_clear", command=lambda: myselect_clear(self,self.mye1))
        self.mybtn4.pack(pady = 5)
        
        self.mybtn5 = Button(self, text="select_present", command=lambda: myselect_present(self,self.mye1))
        self.mybtn5.pack(pady = 5)
        
        def myselect_to(self, myentry):
            myentry.select_to(4)

        def myselect_from(self, myentry):
            myentry.select_from(1)

        def myselect_range(self, myentry):
            myentry.select_range(6,9)

        def myselect_clear(self, myentry):
            myentry.select_clear()
        
        def myselect_present(self, myentry):
            print(myentry.select_present())

if __name__ == "__main__":
    myroot = MySelectMethods ()
    myroot.geometry('400x200')
    myroot.mainloop()
