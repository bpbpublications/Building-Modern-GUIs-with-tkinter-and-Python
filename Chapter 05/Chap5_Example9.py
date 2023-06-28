from tkinter import *

class MyAcessChangeOption(Tk):
    def __init__(self):
        super().__init__()
        self.title('Displaying key values of a tkinter label')
        myl2= Label(self,text = 'Python', bd = 2, bg = 'LightBlue',relief = 'solid',font = ('Verdana',12),
                    width = 12,height = 4,anchor = SE,justify = RIGHT)
        myl2.pack()

        for loop in myl2.keys():
            print(loop,':',myl2[loop]) # will display default values if not mentioned.

if __name__ == "__main__":
    myroot = MyAcessChangeOption()
    myroot.geometry('450x130')
    myroot.mainloop()
