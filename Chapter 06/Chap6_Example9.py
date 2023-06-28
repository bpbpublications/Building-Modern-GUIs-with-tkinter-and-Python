from tkinter import *  
  
myroot = Tk()  
myroot.geometry("250x250")  
  
def mynavigate():  
    # top level object for creation of a new window
    mytopobj = Toplevel(myroot) 
    mytopobj.geometry('250x250')
    #getting the title for the window
    mytopobj.title('NewWindow')
    # infinitely running mainloop
    mytopobj.mainloop()  

# button object for opening of new window on button click
mybtn1 = Button(myroot, text = "Mynavigate", command = mynavigate)  
# positioning the button
mybtn1.place(x=100,y=100)  

# infinitely running mainloop  
myroot.mainloop() 
