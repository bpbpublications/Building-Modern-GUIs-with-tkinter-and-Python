from tkinter import *
myroot  = Tk()

def myselect():
    mychk2.select()
    mychk2['selectcolor'] = 'LightGreen'
    
def mydeselect():
    mychk2.deselect()
    mychk2['bg'] = 'Red'

mychk1 = Radiobutton(myroot, text = 'RadioButton1', indicatoron = True, value = 2)
mychk1.place(x = 50)
mychk1.invoke()

mychk2 = Radiobutton(myroot, text = 'RadioButton2', indicatoron = False, value = 1)
mychk2.place(x = 50, y = 50)

mybtn1 = Button(myroot, text = 'Select', command = myselect)
mybtn1.place(x = 50, y = 100)

mybtn2 = Button(myroot, text = 'Deselect', command = mydeselect)
mybtn2.place(x = 50, y = 150)

myroot.mainloop()
