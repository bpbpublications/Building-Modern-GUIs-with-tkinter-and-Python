from tkinter import *

class Scrollbar_Canvas(Tk):
    def __init__(self): 
        super().__init__()

        mycanvas = Canvas(self, width=150, height=50)
        mycanvas.create_oval(20, 20, 80, 80, fill="red")
        mycanvas.create_oval(200, 200, 280, 280, fill="blue")
        mycanvas.grid(row=0, column=0)

        myscroll_x = Scrollbar(self, orient="horizontal", command=mycanvas.xview)
        myscroll_x.grid(row=1, column=0, sticky=EW)

        myscroll_y = Scrollbar(self,  command=mycanvas.yview)
        myscroll_y.grid(row=0, column=1, sticky=NS)

        mycanvas.configure(scrollregion=mycanvas.bbox("all")) # will return  the rectangular coordinates fitting the whole canvas content. Here the position of 2 corners of a rectangle is described which is a scroll region. It is a 4 valued tuple.

if __name__ == '__main__':
    myroot = Scrollbar_Canvas() # creating an instance of Scrollbar_Entry
    myroot.geometry('200x150')
    myroot.mainloop() # infinite loop to run the application
