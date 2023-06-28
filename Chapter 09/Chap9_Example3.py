from  tkinter import *
from tkinter.filedialog import askopenfilename
myroot = Tk()
myroot.title('AskOpenFileName')
myroot.geometry('300x100')
def myopen_file(): 
    myfile = askopenfilename() 
    print(myfile) # display the file name

mybtn1 = Button(myroot, text = 'MyAskOpenFileName', command = myopen_file)
mybtn1.pack(pady = 10)
myroot.mainloop()
