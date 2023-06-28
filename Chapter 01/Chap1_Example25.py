from tkinter import * 
  
# creating blank tkinter window 
myroot = Tk() 
  
myroot.geometry('300x150+400+400') 
  
mybtn = Button(myroot, text = 'Python') 
mybtn.pack(side = TOP, padx = 5, pady = 5) 
  
myroot.mainloop() 
