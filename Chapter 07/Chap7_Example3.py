from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('350x350')
myroot.title('My ListBox delete')

# creation of listbox with specifed width and height
mylb1 = Listbox(myroot, width = 30, height = 15, font = ('Verdana',12)) # default width = 20 no. of characters in one line and height = 10 (no. of lines)
# insertion of one or more lines into the listbox specified by index
mylb1.insert(1,'Hindi')
mylb1.insert(2,'English')
mylb1.insert(3,'Telugu')
mylb1.insert(4,'Tamil')
mylb1.pack()

# the item selected will be deleted from the listbox
mybtn1 = Button(myroot, text = 'Mydelete', command = lambda mylb1=mylb1: mylb1.delete(ANCHOR))
mybtn1.pack()

def mysize():
    print(mylb1.size())

# the item selected will be deleted from the listbox
mybtn2 = Button(myroot, text = 'Mysize', command = mysize )
mybtn2.pack()

myroot.mainloop() # display window until we press the close button
