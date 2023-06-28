from tkinter import *

class Scrollbar_Entry(Tk):
    def __init__(self): 
        super().__init__()

        self.sclhbar = Scrollbar(self,orient = HORIZONTAL) 
        self.sclhbar.pack(side = BOTTOM,fill = X) 

        self.mye1 = Entry(self,xscrollcommand=self.sclhbar.set) # creation of entry and horizontal scrollbars is attached
        self.mye1.pack(expand = 0, fill=BOTH)

        # horizontal elements
        for loop in range(26): # insertelements from 0 to 49 in the listbox
            self.mye1.insert(END, str(loop) + '\t')
        self.sclhbar.config(command=self.mye1.xview)# for need of horizontal view settings scrollbar command option to entry.xview method

if __name__ == '__main__':
    myroot = Scrollbar_Entry() # creating an instance of Scrollbar_Entry
    myroot.geometry('300x100')
    myroot.mainloop() # infinite loop to run the application
