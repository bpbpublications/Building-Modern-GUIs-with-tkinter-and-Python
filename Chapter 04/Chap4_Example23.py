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

# 1st par: Name of the tag which will be created as a string
# 2nd par: start
# 3rd par: end
mytext.tag_add('mytag1','1.0','1.0 wordend')

# Now, we can configure properties about the tag using tag_configure
mytext.tag_configure('mytag1', background = 'Pink')

myroot.mainloop()
