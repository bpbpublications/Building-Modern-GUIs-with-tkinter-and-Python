from  tkinter import *
from tkinter.filedialog import askopenfilenames
myroot = Tk()
myroot.title('AskOpenFileNames')
myroot.geometry('300x100')
def myopen_files(): 
    myfile_list=[]
    myfiles = askopenfilenames(initialdir="E:\\GUI_Python", title="Select Python files")
    for file in myfiles:
        myfile_list.append(file)
    print(myfile_list)

mybtn1 = Button(myroot, text = 'MyAskOpenFileNames', command = myopen_files)
mybtn1.pack(pady = 10)
myroot.mainloop()
