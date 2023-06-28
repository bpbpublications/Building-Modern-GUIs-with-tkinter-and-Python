from tkinter import *  
  
myroot = Tk()  
myroot.geometry("300x300")  
myroot.title('Main window')
mytopobj = Toplevel(myroot)

mytopobj.title('New window')

mytopobj.geometry("400x400+50+100")  
mytopobj.lift(myroot)
mytopobj.maxsize(400,400)
mytopobj.minsize(200,200)

# infinitely running mainloop  
myroot.mainloop()
