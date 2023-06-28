from tkinter import *

class MyAcessOption(Tk):
    def __init__(self):
        super().__init__()
        self.title('Access options of a tkinter label')
        myl2= Label(self,text = 'Stay\nSafe From\nFrom Corona Virus', bd = 2, bg = 'LightGreen',                    relief = 'solid',
                    font = ('Arial',14),width = 20,height = 4,anchor = NW,justify = LEFT)
        myl2.pack()
        print(myl2["text"])
        print("--------")
        print(myl2["bd"])
        print(myl2["bg"])
        print(myl2["font"])
        print(myl2["width"])
        print(myl2["height"])
        print(myl2["anchor"])
        print(myl2["justify"])
        
if __name__ == "__main__":
    myroot = MyAcessOption()
    myroot.geometry('350x150')
    myroot.mainloop()
