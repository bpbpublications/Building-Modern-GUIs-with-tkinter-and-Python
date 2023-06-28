from tkinter import *

class MyPadSpace(Tk):
    def __init__(self):
        super().__init__()
        self.title('Pad space around the text')
        myl1 = Label(self, text = 'Python')
        myl1.pack()
        myl2= Label(self, text = 'Stay\Safe',bd = 4, relief = 'groove',font = ('Verdana',12))
        myl2.pack()
        myl3 = Label(self, text = 'Python')
        myl3.pack()
        myl4= Label(self,text = 'Stay\Safe',bd = 4, relief = 'groove',font = ('Verdana',12),padx = 20)
        myl4.pack()
        myl5 = Label(self, text = 'Python')
        myl5.pack()
        myl6= Label(self,text = 'Stay\Safe',bd = 4, relief = 'groove',font = ('Verdana',12),pady = 10)
        myl6.pack()
        myl7 = Label(self, text = 'Python')
        myl7.pack()
        myl8= Label(self,text = 'Stay\Safe',bd = 4, relief = 'groove',font = ('Verdana',12),padx = 10, pady = 10)
        myl8.pack()
        
if __name__ == "__main__":
    myroot = MyPadSpace()
    myroot.geometry('350x300')
    myroot.mainloop()
