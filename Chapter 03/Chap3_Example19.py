from tkinter import *
myroot  = Tk()
def selectcolor_indicatoronTrue():
    mychk1['selectcolor'] = 'Green'

def selectcolor_indicatoronFalse():
    mychk2['selectcolor'] = 'Blue'

mychk1 = Checkbutton(myroot, text = 'CheckButton', command = selectcolor_indicatoronTrue, indicatoron = True)
mychk1.place(x = 50, y = 50)
mychk2 = Checkbutton(myroot, text = 'CheckButton', command = selectcolor_indicatoronFalse, indicatoron = False)
mychk2.place(x = 50, y = 100)
myroot.mainloop()
