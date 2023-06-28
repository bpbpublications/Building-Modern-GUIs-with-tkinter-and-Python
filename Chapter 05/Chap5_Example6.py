from tkinter import *

class MyAnchorJustify(Tk):
    def __init__(self):
        super().__init__()
        self.title('Anchor and Jusify in label')
        myl1 = Label(self, text = 'Anchor and Justify in Right')
        myl1.pack()
        myl2= Label(self, 
                    text = 'Stay\nSafe Safe\nSafe Safe Safe',bd = 2, relief = 'solid',font = ('Times New Roman',12),
                    width = 20,height = 4,anchor = NE, justify = RIGHT)
        myl2.pack()
        myl3 = Label(self, text = 'Anchor and Justify in Left')
        myl3.pack()
        myl4= Label(self,text = 'Stay\nSafe Safe\nSafe Safe Safe', bd = 2, relief = 'solid',
                    font = ('Times New Roman',12),width = 20,height = 4,anchor = NE,justify = LEFT)
        myl4.pack()

if __name__ == "__main__":
    myroot = MyAnchorJustify()
    myroot.geometry('350x300')
    myroot.mainloop()
