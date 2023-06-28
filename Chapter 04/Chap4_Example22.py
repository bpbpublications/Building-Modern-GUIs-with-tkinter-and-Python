from tkinter import * # importing module
from tkinter import messagebox

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('400x350')
myroot.title('Textwidget')

# creation of text widget
mytext = Text(myroot, width = 18, height = 10, font = ('Calibri',12), wrap = WORD, padx = 10, pady = 10, bd = 4, selectbackground = 'Green', selectforeground = 'Red')
mytext.pack()

#inserting text in the text widget
mytext.insert('1.0', 'Hey Beginners! Welcome for the learning of python text widget. \n This is another line')

# inserting text in the third line
mytext.insert('1.0 + 2 lines', '\nThis is 3rd line')

# callback function
def myget():
    messagebox.showinfo('First line contents in the text widget  are: ',mytext.get('1.0', '1.end')) # we are reading the contents of first line only

# creation of button widget
mybtn1 = Button(myroot, text = 'Read', command = myget)
mybtn1.pack()

def mydelete():
    mytext.delete('1.0')

# creation of Delete button for single characterwidget
mybtn2 = Button(myroot, text = 'DeleteSingleCharacter', command = mydelete)
mybtn2.pack(pady = 10)

def mydelete_entireline():
    mytext.delete('1.0','1.0 lineend')

# creation of Delete button for entire line widget
mybtn2 = Button(myroot, text = 'DeleteEntireLine', command = mydelete_entireline)
mybtn2.pack(pady = 10)

myroot.mainloop() # display window until we press the close button
