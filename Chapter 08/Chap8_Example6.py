from tkinter import *    
myroot = Tk()
myroot.geometry('200x200')

# Create a menu button with optiones specified
gamelist = Menubutton(myroot, text='Games', justify=CENTER, relief = 'groove')

# creating drop down menu which will become visible when the user will click the menu button
mygames   = Menu(gamelist)               
gamelist.config(menu=mygames)

# will add commands to the drop down menu
mygames.add_command(label='Cricket')
mygames.add_command(label='Football')
mygames.add_command(label='Badminton')

gamelist.pack()
myroot.mainloop()
