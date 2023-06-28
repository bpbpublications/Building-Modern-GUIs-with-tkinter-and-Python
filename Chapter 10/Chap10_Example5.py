from tkinter import * 

myroot = Tk() 

def myx_y_func():
    print(mybtn2.winfo_x())
    print(mybtn2.winfo_y())
    
mybtn2 = Button(myroot, text = "Button", command = myx_y_func, bg = 'LightGreen') 
mybtn2.pack(pady = 10) 

myroot.geometry('300x100')
myroot.mainloop()