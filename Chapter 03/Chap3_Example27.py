from tkinter import *
myroot = Tk()

myrb1 = Radiobutton(myroot, value=0, text="RadioButton1", bg = 'lightGreen', indicatoron=False,)
myrb2 = Radiobutton(myroot, value=1,text="RadioButton2",bg = 'lightGreen',  indicatoron=False)

myrb1.pack(padx=10, pady=10)
myrb2.pack(padx=10, pady=10)

myroot.mainloop()
