from tkinter import * 
from tkinter import messagebox
myroot = Tk() 

def mydisplay():
    messagebox.showinfo('Message',"Python")
    
mybtn = Button(myroot, text="Display",command=mydisplay) 
mybtn.pack(padx=20, pady=30)
myroot.mainloop()
