from tkinter import *  
  
myroot = Tk()  
myroot.geometry("250x250")  
  
def mynavigate():  
    # top level object for creation of a new window
    mytopobj1 = Toplevel(myroot) 
    mytopobj1.geometry('250x250')
    #getting the title for the window
    mytopobj1.title('MyToplevel1')
    
    myl1 = Label(mytopobj1, text = 'This is a toplevel1 window')
    myl1.pack(pady = 10)
    
    mybtn1 = Button(mytopobj1, text = 'MyToplevel2 window', command = func_mytoplevel2)
    mybtn1.pack(pady = 10)
    
    mybtn2 = Button(mytopobj1, text = 'Exit', command = mytopobj1.destroy)
    mybtn2.pack(pady = 10)
    
    # infinitely running mainloop
    mytopobj1.mainloop() 
    
def func_mytoplevel2():
    # top level object for creation of a new window
    mytopobj2 = Toplevel(myroot) 
    mytopobj2.geometry('250x250')
    #getting the title for the window
    mytopobj2.title('MyToplevel2')
    
    myl1 = Label(mytopobj2, text = 'This is a toplevel2 window')
    myl1.pack(pady = 10)
    
    mybtn2 = Button(mytopobj2, text = 'Exit2', command = mytopobj2.destroy)
    mybtn2.pack(pady = 10)
    
    # infinitely running mainloop
    mytopobj2.mainloop() 

# button object for opening of new window on button click
mybtn1 = Button(myroot, text = "MyToplevel1", command = mynavigate)  
# positioning the button
mybtn1.place(x=100,y=100)  

# infinitely running mainloop  
myroot.mainloop()
