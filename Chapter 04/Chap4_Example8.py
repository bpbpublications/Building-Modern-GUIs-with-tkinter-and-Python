from tkinter import *
class MyValidate(Tk):
    def __init__(self):
        super().__init__()
        self.myl0 = Label(self, text= 'Enter the number:', fg='Magenta', font = ('Arial',12))
        self.myl0.place(x = 10, y = 30)
        
        self.mye1 = Entry(self, font = ('Helvetica',12)) 
        self.mye1.place(x = 150, y = 30) 
        
        self.myl1 = Label(self, text= '', fg='Red')
        self.myl1.place(x = 70, y = 50)
        
        self.myreg = self.register(self.mycallback) # V1
        self.invalidcmd = self.register(self.myinvalid_name) # V2
        self.mye1.config(validate ="key",  validatecommand =(self.myreg, '%P'), invalidcommand = (self.invalidcmd, '%S'))  # V3
        
    def mycallback(self, myinp): 
        if myinp.isdigit():# C1
            print(myinp) 
            self.myl1.config(text='')
            return True
                            
        elif myinp is "": # C2
            print(myinp) 
            self.myl1.config(text='')
            return True
    
        else: # C3
            print(myinp) 
            return False
    
    def myinvalid_name(self, myCh):
        self.myl1.config(text=(f'Invalid character {myCh} \n name can only have numbers'), font = ('Verdana',10))

if __name__ == "__main__":
    myroot = MyValidate()
    myroot.geometry('300x100')
    myroot.mainloop()
