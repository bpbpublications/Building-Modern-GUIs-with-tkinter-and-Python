from  tkinter import *
from tkinter.filedialog import askdirectory
myroot = Tk()
myroot.title('Askdirectory')
myroot.geometry('300x100')
def mydisplay():
    myroot.directory = askdirectory()

mybtn1 = Button(myroot, text = 'MyDirectoryOpen', command = mydisplay)
mybtn1.pack(pady = 10)
myroot.mainloop()
