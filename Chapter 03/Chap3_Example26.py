from tkinter import *
myroot = Tk()

myon_image = PhotoImage(width=50, height=25)
myoff_image = PhotoImage(width=50, height=25)
myon_image.put(("LightGreen",), to=(0, 0, 24,24)) # It will put row formatted colors to image starting from position TO
myoff_image.put(("Red",), to=(0, 0, 24, 24))

myrbvar = IntVar(value=1)
myrb1 = Radiobutton(myroot, variable=myrbvar, value=0, bd=0, 
                     text="RadioButton1", compound="left", indicatoron=False, 
                     image=myoff_image, selectimage=myon_image)
myrb2 = Radiobutton(myroot, variable=myrbvar, value=1,  bd=0, 
                     text="RadioButton2", compound="left", indicatoron=False,
                     image=myoff_image, selectimage=myon_image)

myrb1.pack(padx=10, pady=10)
myrb2.pack(padx=10, pady=10)

myroot.mainloop()
