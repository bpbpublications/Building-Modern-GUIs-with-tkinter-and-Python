from tkinter import *
 
myroot = Tk() 
myroot.geometry('350x200')
myroot.title("StatusBarExample")

mystatusbar = Label(myroot, text="It is a statusbar example...", bd=1, relief=SUNKEN, anchor=W) # where bd: bordersize , relief: label appearance, anchor: text alignment within the label

mystatusbar.pack(side=BOTTOM, fill=X) # positioned at the GUI bottom and covers the whole window width if window is resized
myroot.mainloop()
