from tkinter import *

class MyImage(Frame):
    def __init__(self, root = None):
        Frame.__init__(self, root)
        self.root = root
        self.myphoto = PhotoImage(file = 'butterfly1.gif')
        self.myl1 = Label(self.root,image = self.myphoto)
        self.myl1.pack(padx = 10, pady = 10)
        
if __name__ == "__main__":
    myroot = Tk()
    myobj = MyImage(myroot)
    myroot.title('Image using label')
    myroot.geometry('300x300')
    myroot.mainloop()
