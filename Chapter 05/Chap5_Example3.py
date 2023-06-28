from tkinter import *

class MyLabelPosition(Tk):
    def __init__(self):
        super().__init__()
        self.title('Position Text within a label')
        self.myl2= Label(self, text = 'Hello\nThere',bd = 4, relief = 'groove', font = 'Times 32', width = 10,
            height = 4, anchor = SW)
        self.myl2.pack()

if __name__ == "__main__":
    myroot = MyLabelPosition()
    myroot.mainloop()
