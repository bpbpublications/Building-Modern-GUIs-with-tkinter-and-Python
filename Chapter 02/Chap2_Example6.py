from tkinter import * 
from tkinter import messagebox
 
class MyBtn(Tk): 
    def __init__(self): # constructor
        super().__init__() # for calling the constructor of superclass
        self.mybtn = Button(self, text="Display", command=self.mydisplay) 
        self.mybtn.pack(padx=20, pady=30) 
 
    def mydisplay(self):
        messagebox.showinfo('Message',"Python")
 
if __name__ == "__main__": 
    myroot = MyBtn() # making an object of MyBtn class
    myroot.mainloop()
