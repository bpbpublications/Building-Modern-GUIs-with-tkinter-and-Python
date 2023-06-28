from tkinter import *

class MyAcessChangeOption(Tk):
    def __init__(self):
        super().__init__()
        self.title('Access and Change options of a tkinter label')
        myl2= Label(self,text = 'Stay\nSafe From\nFrom Corona Virus', bd = 2, bg = 'LightGreen', fg = 'Yellow',                   relief = 'solid',
                    font = ('Arial',14),width = 20,height = 4,anchor = NW,justify = LEFT)
        myl2.pack()
        myl2["bg"] = 'LightBlue' # we are changing bg to LightBlue
        myl2["fg"] = 'Red'# we are changing fg to Red

if __name__ == "__main__":
    myroot = MyAcessChangeOption()
    myroot.geometry('450x130')
    myroot.mainloop()
