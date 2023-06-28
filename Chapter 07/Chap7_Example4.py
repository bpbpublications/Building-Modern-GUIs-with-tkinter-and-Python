from tkinter import *

class Scrollbar_Listbox(Tk):
    def __init__(self): 
        super().__init__()
        self.title('V AND H SCROLLBARS')

        self.mysclbar = Scrollbar(self)# scrollbar creation and attaching to the main window
        self.mysclbar.pack(side=RIGHT, fill=Y) # scrollbar added to the window right side
        
        self.sclhbar = Scrollbar(self,orient = HORIZONTAL) 
        self.sclhbar.pack(side = BOTTOM,fill = X) 

        self.mylistbox = Listbox(self, 
                          height = 600, 
                          yscrollcommand=self.mysclbar.set,
                          xscrollcommand=self.sclhbar.set) # creation of listbox and both horizontal and vertical scrollbars are attached to the listbox
        
        self.mylistbox.pack(expand = 0, fill=BOTH)
       
        # horizontal elements
        for loop in range(26): # insertelements from 0 to 49 in the listbox
            self.mylistbox.insert(END, 'The element is staring from line number ' + str(loop) + ' and when multiplied by 10 is: ' + str(loop*10))
        # vertical elements
        for loop in range(50): # insertelements from 0 to 49 in the listbox
            self.mylistbox.insert(END, str(loop) + '\n')
                
        self.sclhbar.config(command=self.mylistbox.xview)# for need of horizontal view settings scrollbar command option to listbox.xview method
        self.mysclbar.config(command=self.mylistbox.yview) # for need of vertical view settings scrollbar command option to listbox.yview method

if __name__ == '__main__':
    myroot = Scrollbar_Listbox() # creating an instance of Scrollbar_Listbox
    myroot.geometry('300x500')
    myroot.mainloop() # infinite loop to run the application
