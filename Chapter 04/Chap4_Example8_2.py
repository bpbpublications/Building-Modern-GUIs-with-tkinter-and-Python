from tkinter import *

myroot = Tk()
myroot.geometry('300x100')

myl0 = Label(myroot, text= 'Enter the number:', fg='Magenta', font = ('Arial',12))
myl0.place(x = 10, y = 30)
mye1 = Entry(myroot, font = ('Helvetica',12)) 
mye1.place(x = 150, y = 30) 
myl1 = Label(myroot, text= '', fg='Red')
myl1.place(x = 70, y = 50)

def mycallback(myinp): 
    if myinp.isdigit():
        print(myinp) 
        myl1.config(text='')
        return True
                        
    elif myinp is "":
        print(myinp) 
        myl1.config(text='')
        return True

    else:
        print(myinp) 
        return False
    
def myinvalid_name(myCh):
        myl1.config(text=(f'Invalid character {myCh} \n name can only have numbers'), font = ('Verdana',10))

myreg = myroot.register(mycallback)
invalidcmd = myroot.register(myinvalid_name)
mye1.config(validate ="key",  validatecommand =(myreg, '%P'), invalidcommand = (invalidcmd, '%S'))
    
myroot.mainloop()
