from tkinter import *

class MyLabelFrame(Tk):
    def __init__(self): 
        super().__init__()
        
        # labelframe is defined and the text is assigned to be displayed by the frame.
        self.mylf1 = LabelFrame(self, text="Welcome to Label and ButtonFrame ", font = ('Calibri',12), bg = 'LightBlue')
        self.mylf1.pack(fill="both", expand="yes")
        
        #Label is defined and created
        self.myl1 = Label(self.mylf1, text="I am Label", bg = 'Magenta')
        self.myl1.pack(side = TOP)
        
        #Button is defined and created
        self.mybtn1 = Button(self.mylf1, text="I am Button", bg = 'Violet')
        self.mybtn1.pack(side = LEFT)
        
        # labelframe is defined and the text is assigned to be displayed by the frame.
        self.mylf2 = LabelFrame(self, text="Welcome to CheckButton and Radiobutton Frame", font = ('Calibri',12), bg = 'LightGreen')
        self.mylf2.pack(fill="both", expand="yes")
        
        #Checkbutton is defined and created
        self.mychk1 = Checkbutton(self.mylf2, text="I am CheckButton", bg = 'Pink')
        self.mychk1.pack(side = RIGHT)
        
        #RadioButton is defined and created
        self.myr1 = Radiobutton(self.mylf2, text="I am RadioButton", bg = 'Brown')
        self.myr1.pack(side = BOTTOM)

if __name__ == '__main__':
    myroot = MyLabelFrame() # creating an instance of MyLabelFrame
    myroot.geometry('400x150')
    myroot.mainloop() # infinite loop to run the application
