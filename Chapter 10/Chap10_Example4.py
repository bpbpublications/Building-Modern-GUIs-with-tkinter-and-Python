from tkinter import * 

myroot = Tk() 
  
def myforget(widget): 
    widget.forget() 
    print(f"Is {widget['text']} mapped after calling forget method ? = ", 
                               bool(widget.winfo_ismapped())) 
  
def myretrieve(widget): 
    widget.pack() 
    # will check if the widget exists or not
    print(f"Is {widget['text']} mapped after widget retrieval ? = ", 
                                bool(widget.winfo_exists())) 

mybtn1 = Button(myroot, text = "IamButton1", bg = 'LightBlue') 
mybtn1.pack(pady = 10) 
  
# Making widget invisible 
mybtn2 = Button(myroot, text = "Button2", command = lambda : myforget(mybtn1), bg = 'LightGreen') 
mybtn2.pack(pady = 10) 
   
# Retrieving the widget 
mybtn3 = Button(myroot, text = "Button3", command = lambda : myretrieve(mybtn1), bg = 'LightPink') 
mybtn3.pack(pady = 10) 

myroot.geometry('300x200')
  
myroot.mainloop()