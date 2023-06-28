from tkinter import *
myroot  = Tk()
def selectcolor_indicatoronTrue():
    mychk1['selectcolor'] = 'LightGreen'

def selectcolor_indicatoronFalse():
    mychk2['selectcolor'] = 'Blue'

mychk1 = Radiobutton(myroot, text = 'RadioButton1', command = selectcolor_indicatoronTrue, indicatoron = True, value = 1)
mychk1.place(x = 50, y = 50)
mychk2 = Radiobutton(myroot, text = 'RadioButton2', command = selectcolor_indicatoronFalse, indicatoron = False, value = 2)
mychk2.place(x = 50, y = 100)
myroot.mainloop()
