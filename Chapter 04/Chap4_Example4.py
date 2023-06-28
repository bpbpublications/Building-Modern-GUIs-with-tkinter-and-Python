from tkinter import *

class MyCursorPosition(Tk):
     def __init__(self):
        super().__init__()
        self.title('MyCursorPosition Example')
        self.mye1= Entry(self,font = ('Arial',12),width = 20, bd = 5)
        self.mye1.pack(side = LEFT)
        self.mye1.focus()
        self.mye1.insert(0,'Demonstration')
        self.mye1.icursor(0)
               
        self.button1 = Button(self, text="Position the cursor", command=lambda: myposition(self,self.mye1))
        self.button1.pack(pady = 32)
        
        def myposition(self, myentry):
            myentry.icursor(3)

if __name__ == "__main__":
    myroot = MyCursorPosition()
    myroot.geometry('400x100')
    myroot.mainloop()
