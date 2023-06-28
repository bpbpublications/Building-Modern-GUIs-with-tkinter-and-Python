from tkinter import * # importing module

myroot = Tk() # window creation and initialize the interpreter
myroot.geometry('300x330')
myroot.title('Textwidget')

# creation of text widget
mytext = Text(myroot, width = 15, height = 10, font = ('Calibri',12), wrap = WORD, padx = 10, pady = 10, bd = 4, selectbackground = 'Green', selectforeground = 'Red')
mytext.pack()

mytext.insert('1.0', 'This is 1st line')
mytext.insert('1.0 + 1 line', '\nThis is 2nd line')

def myinsert_mark():
    mytext.insert('insert','@') # will insert '@' at the position of the insert marker

mybtn2 = Button(myroot, text = 'InsertMark', command = myinsert_mark)
mybtn2.pack(pady = 10)

myroot.mainloop()
