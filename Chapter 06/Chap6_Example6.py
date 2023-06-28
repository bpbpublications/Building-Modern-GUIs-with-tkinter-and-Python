from tkinter import * 
from tkinter import ttk 

myroot = Tk() 
myroot.title("Demo Tab Widget") 
mytabcontrol = ttk.Notebook(myroot) # L1
  
mytab1 = ttk.Frame(mytabcontrol) # L2
mytab2 = ttk.Frame(mytabcontrol) 
  
mytabcontrol.add(mytab1, text ='MyTab1') # L3
mytabcontrol.add(mytab2, text ='MyTab2') 

mytabcontrol.pack(expand = 1, fill ="both")   # L4

ttk.Label(mytab1, text ="Welcome to Tab1", font = ('Helvetica',12)).grid(column = 0,row = 0, padx = 50, pady = 50) # L5
ttk.Label(mytab2, text ="I hope u now understood the tab concept now", font = ('Times New Roman',12)).grid(column = 0, row = 0, padx = 50, pady = 50) 
  
myroot.mainloop() 
