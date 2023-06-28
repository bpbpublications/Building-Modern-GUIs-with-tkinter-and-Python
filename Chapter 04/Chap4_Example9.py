from tkinter import *

class Scrollbar_ListBox(Tk):
    def __init__(self): 
        super().__init__()

        self.mysclbar = Scrollbar(self)# scrollbar creation and attaching to the main window
        self.mysclbar.pack(side=RIGHT, fill="y") # scrollbar added to the window right side

        self.mylstbox = Listbox(self)# listbox creation and attaching to the main window
        self.mylstbox.config(yscrollcommand=self.mysclbar.set) # scrollbar attached to the listbox . for vertical scroll used yscrollcommand
        
        for loop in range(50): # insertelements from 0 to 49 in the listbox
            self.mylstbox.insert(END, str(loop))

        self.mylstbox.pack(side="left", fill=BOTH) # listbox added to the window left side
        self.mysclbar.config(command=self.mylstbox.yview) # for need of vertical view settings scrollbar command option to listbox.yview method

if __name__ == '__main__':
    myroot = Scrollbar_ListBox() # creating an instance of Scrollbar_Listbox
    myroot.mainloop() # infinite loop to run the application
