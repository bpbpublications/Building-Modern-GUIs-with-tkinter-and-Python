from tkinter import * # importing module
from tkinter import messagebox

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('400x250')
myroot.title('Textwidget')

# creation of text widget
mytext = Text(myroot, width = 18, height = 10, font = ('Calibri',12), wrap = WORD, padx = 10, pady = 10, bd = 4, selectbackground = 'Green', selectforeground = 'Red')
mytext.pack()

#inserting text in the text widget
mytext.insert('1.0', 'Hey Beginners! Welcome for the learning of python text widget. \n This is another line')

# callback function
def myget():
    messagebox.showinfo('Text widget contents are: ',mytext.get('1.0', 'end'))  # we are reading the entire contents of the text widget and displaying
# creation of button widget
mybtn1 = Button(myroot, text = 'Read', command = myget)
mybtn1.pack()

myroot.mainloop() # display window until we press the close button
