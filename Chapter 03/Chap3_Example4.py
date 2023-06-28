from tkinter import * # importing module
class MyLeftRightMouseClick(Tk):
    def __init__(self):
        super().__init__()
        self.title('Button Left and Right click')
        
        def mycall(event):
            print('Left Clicked')
        
        def mycallme(event):
            print('Right Clicked')
        
        self.myb1 = Button(self, text = 'LeftClick', font = ('Calibri',15))
        self.myb1.bind('<Button-1>', mycall) # Left click
        self.myb1.pack(pady = 10) # for displaying the button
        
        self.myb2 = Button(self, text = 'RightClick', font = ('Calibri',15))
        self.myb2.bind('<Button-3>', mycallme) # Right click
        self.myb2.pack(pady = 10) # for displaying the button

if __name__ == "__main__":
    myroot = MyLeftRightMouseClick()
    myroot.geometry('350x150')
    myroot.mainloop() # display window until we press the close button
