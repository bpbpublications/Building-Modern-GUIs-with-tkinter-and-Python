from  tkinter import *
from tkinter.filedialog import askopenfile
myroot = Tk()
myroot.title('AskOpenFile')
myroot.geometry('300x100')
def myopen_file(): 
    myfile = askopenfile(mode ='r', filetypes =[('All Python Files', '*.py')]) 
    if myfile is not None: 
        content = myfile.read() # read all the file contents
        print(myfile.name) # display the file name
mybtn1 = Button(myroot, text = 'MyAskOpenFile', command = myopen_file)
mybtn1.pack(pady = 10)
myroot.mainloop()
