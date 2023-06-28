from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('350x350')
myroot.title('My ListBox')

def myget():
    mylinenumber = mylb1.curselection() # getting the line number
    for loop in mylinenumber:
        print(loop, ':', mylb1.get(loop)) # getting the item of that line number

# creation of listbox with specifed width and height
mylb1 = Listbox(myroot, width = 30, height = 15, bg = 'LightGreen', font = ('Verdana',12)) # default width = 20 no. of characters in one line and height = 10 (no. of lines)
# insertion of one or more lines into the listbox specified by index
mylb1.insert(1,'Hindi')
mylb1.insert(2,'English')
mylb1.insert(3,'Telugu')	
mylb1.pack()

mybtn = Button(myroot, text = 'Line number display', command = myget)
mybtn.pack()

myroot.mainloop() # display window until we press the close button
