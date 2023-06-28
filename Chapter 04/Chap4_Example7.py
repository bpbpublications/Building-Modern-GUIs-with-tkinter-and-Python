from tkinter import *

class MyScrollbarEntry(Tk):
     def __init__(self):
        super().__init__()
        mysobj_scroll = Scrollbar(self,orient = 'horizontal')
        mye1 = Entry(self,xscrollcommand = mysobj_scroll.set, font = ('Calibri',12))
        mye1.focus()
        mye1.pack(side= 'bottom', fill = X)
        mysobj_scroll.pack(fill = X)
        mysobj_scroll.config(command = mye1.xview)
        mye1.config()
        mye1.insert(0, 'We should follow social distancing when we are going outside from our home. It is mandatory to follow.')

if __name__ == "__main__":
    myroot = MyScrollbarEntry()
    myroot.geometry('400x200')
    myroot.mainloop()
