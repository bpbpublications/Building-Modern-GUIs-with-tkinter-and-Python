from tkinter import *  
  
myroot = Tk()  
myroot.geometry("300x300")  
myroot.title('Main window')
mytopobj = Toplevel(myroot)

mytopobj.title('New window')

mytopobj.geometry("400x300+50+100")  
mytopobj.lift(myroot)
mytopobj.deiconify()

# infinitely running mainloop  
myroot.mainloop() 
