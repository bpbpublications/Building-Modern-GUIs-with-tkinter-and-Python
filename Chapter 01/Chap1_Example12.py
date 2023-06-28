from tkinter import *
myroot = Tk()
mye1 = Entry(myroot, bg='LightGreen', highlightthickness=10, highlightbackground="red", highlightcolor = 'Yellow')
mye1.pack(padx=5, pady=5)
mye2 = Entry(myroot)
mye2.pack()
mye2.focus()
myroot.mainloop()
