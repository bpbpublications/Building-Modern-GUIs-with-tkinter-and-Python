from tkinter import *
myroot = Tk() 
myroot.title('Trace_add')
myroot.geometry('300x200')

my_value = StringVar() 

mybtn1 = Button(myroot, textvariable = my_value, bg = 'LightBlue')
mybtn1.pack(padx = 10, pady = 10) 

mye1 = Entry(myroot, textvariable = my_value, bg = 'LightGreen')
mye1.pack(padx = 10, pady = 10) 

# defining the callback function (observer) 
def my_associatedcallback(var, indx, mode): 
    print("Traced variable {}: ".format(my_value.get())) 
        
# registering the observer 
my_value.trace_add('write', my_associatedcallback) 

myroot.mainloop() 
