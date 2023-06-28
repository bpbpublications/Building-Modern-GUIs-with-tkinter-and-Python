from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('300x300')
myroot.title('Textwidget')

# creation of text widget
mytext = Text(myroot, width = 18, height = 10, font = ('Calibri',12), wrap = WORD, padx = 10, pady = 10, bd = 4, selectbackground = 'Green', selectforeground = 'Red')
mytext.pack()

mytext.insert('1.0', 'This is 1st line')
mytext.insert('1.0 + 1 line', '\nThis is 2nd line')
mytext.insert('1.0 + 2 lines', '\nThis is 3rd line')

print(mytext.mark_names()) # by default there are 2 marks that tk automatically keeps track of.

myroot.mainloop()
