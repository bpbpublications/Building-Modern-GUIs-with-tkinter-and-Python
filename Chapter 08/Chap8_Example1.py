from tkinter import *  
  
myroot = Tk()  

# will be called when Welcome! menu item will be clicked
def mygreet():  
    print("Welcome!")  
  
# A toplevel menu is created
mymenu = Menu(myroot)
#menu items will be added to the main menu
mymenu.add_command(label="Welcome!", command=mygreet)
mymenu.add_command(label="Quit!", command=myroot.quit)  # will close the GUI application
  
# display of menu  
myroot.config(menu=mymenu)  
  
myroot.mainloop()  
