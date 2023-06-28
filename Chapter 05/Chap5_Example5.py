from tkinter import *

class MyJustify(Tk):
    def __init__(self):
        super().__init__()
        self.title('Jusify in label')
        myl1 = Label(self, text = 'Python')
        myl1.pack()
        myl2= Label(self, text = 'Hello\nThere There\nThere There There',bd = 2, relief = 'solid',font = ('Helvetica',10))
        # default justify is CENTER
        myl2.pack()
        myl3 = Label(self, text = 'Python')
        myl3.pack()
        myl4= Label(self,text = 'Hello\nThere There\nThere There There',bd = 2, relief = 'solid',font = ('Helvetica',10),
                    justify = LEFT)
        myl4.pack()
        myl5= Label(self,text = 'Hello\nThere There\nThere There There',bd = 2, relief = 'solid',font = ('Helvetica',10),
                    justify = RIGHT)
        myl5.pack()
        
if __name__ == "__main__":
    myroot = MyJustify()
    myroot.geometry('350x300')
    myroot.mainloop()
