from tkinter import * 
myroot = Tk()
myroot.geometry('300x160')
mye1 = Entry(myroot)
mye1.pack(pady = 10)

mybtn1 = Button(myroot, text = 'Button')
mybtn1.pack(pady = 10)

myl1 = Label(myroot, text = 'Label')
myl1.pack(pady = 10)

# we are iterating on each child widget of the parent window and disabling them
for loop in myroot.winfo_children():
    loop.config(state='disable')

myroot.mainloop()