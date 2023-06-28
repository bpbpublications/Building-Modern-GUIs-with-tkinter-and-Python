from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('400x250')
myroot.title('Textwidget')

# creation of text widget
mytext = Text(myroot, width = 18, height = 10, font = ('Calibri',12), wrap = WORD, padx = 10, pady = 10, bd = 4, selectbackground = 'Green', selectforeground = 'Red')
mytext.pack()

myroot.mainloop() # display window until we press the close button
