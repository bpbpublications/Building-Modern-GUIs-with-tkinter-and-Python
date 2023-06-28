from tkinter import *  
  
myroot = Tk()  
myroot.geometry("300x300")  
myroot.title('Main window')
mytopobj = Toplevel(myroot)

mytopobj.title('New window')

mytopobj.geometry("300x300")  
mytopobj.lift(myroot)
mytopobj.state('zoomed')

# infinitely running mainloop  
myroot.mainloop() 

