from tkinter import *

#main window creation
myroot = Tk()

#window size
myroot.geometry('300x300')

#paned window object
mypw1 = PanedWindow(myroot,orient ='vertical')

#expand option for widgets to expand and fill for letting widgets adjust itself
mypw1.pack(fill = BOTH, expand = 1)  

# Checkbutton object
mychk = Checkbutton(mypw1, text ="I am checkbutton") 
mychk.pack(side = TOP) 
  
# Adding Checkbutton to panedwindow 
mypw1.add(mychk) 

# Radiobutton object
myr1 = Radiobutton(mypw1, text ="I am radiobutton") 
myr1.pack(side = TOP) 

# Adding Radiobutton to panedwindow 
mypw1.add(myr1) 

# button object
mybtn1 = Button(mypw1, text ="I am button") 
mybtn1.pack(side = TOP) 

# Adding button to panedwindow 
mypw1.add(mybtn1) 

# Tkinter string variable 
mystr = StringVar() 
  
# entry widget
mye1 = Entry(mypw1, textvariable = mystr, font =('arial', 15, 'bold')) 
mye1.pack() 
  
# will focus on entry widget particularly
mye1.focus_force() 

mystr.set('            PanedWindow')

# Will show sash 
mypw1.configure(sashrelief = RAISED, sashwidth = 5) 

# adding entry widget to the paned window
mypw1.add(mye1) 

#infinite loop
myroot.mainloop()
