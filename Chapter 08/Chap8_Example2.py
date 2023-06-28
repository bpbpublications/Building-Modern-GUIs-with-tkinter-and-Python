from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter

#creating main menu
mymainmenu = Menu(myroot)
myroot.config(menu = mymainmenu) # need to attach the above menu with the root

#creating file menu -- sub level menu corresponding to the main menu
myfilemenu = Menu(mymainmenu, tearoff = 0) # removing the dotted lines by setting tearoff = 0
mymainmenu.add_cascade(label = 'MyFile', menu = myfilemenu)

# function is created to display MyNew Project Menu
def myfunc1():
    print('MyNew Project Menu')

# function is created to display MySave menu
def myfunc3():
    print('MySave Menu')

# function is created to exit the GUI application
def myfunc4():
    print('Exit')
    myroot.quit()
    exit()
    
#adding in the file menu
myfilemenu.add_command(label='MyNew Project', command = myfunc1) # bind the function myfunc1 we created to the above menuitem
myfilemenu.add_command(label='MySave', command = myfunc3) # bind the function myfunc3 we created to the above menuitem
myfilemenu.add_separator() # adding the seperator between MySave and MyExit
myfilemenu.add_command(label='MyExit', command = myfunc4) # bind the function myfunc4 we created to the above menuitem

#creating edit menu-- sub level menu corresponding to the main menu
myeditmenu = Menu(mymainmenu)
mymainmenu.add_cascade(label = 'MyEdit', menu = myeditmenu)

# function is created to display MyUndo menu
def myfunc2():
    print('MyUndo Menu')

# function is created to display MyCut menu
def myfunc5():
    print('MyCut Menu')

# function is created to display MyCopy menu
def myfunc6():
    print('MyCopy Menu')

# function is created to display MyRedo menu
def myfunc7():
    print('MyRedo Menu')
    
#adding in the file menu
myeditmenu.add_command(label='MyCut', command = myfunc5) # bind the function myfunc5 we created to the above menuitem
myeditmenu.add_command(label='MyCopy', command = myfunc6) # bind the function myfunc6 we created to the above menuitem
myeditmenu.add_command(label='MyUndo', command = myfunc2) # bind the function myfunc2 we created to the above menuitem
myeditmenu.add_command(label='MyRedo', command = myfunc7) # bind the function myfunc7 we created to the above menuitem

myroot.mainloop() # display window until we press the close button
