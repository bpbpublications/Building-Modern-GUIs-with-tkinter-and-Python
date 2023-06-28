from tkinter import *
myroot = Tk()

myon_image = PhotoImage(width=50, height=25)
myoff_image = PhotoImage(width=50, height=25)
myon_image.put(("LightGreen",), to=(0, 0, 24,24)) # It will put row formatted colors to image starting from position TO
myoff_image.put(("Red",), to=(25, 0, 49, 24))

myval1 = IntVar(value=0)
myval2 = IntVar(value=1)
cb1 = Checkbutton(myroot, image=myoff_image, selectimage=myon_image, indicatoron=False,
                     onvalue=1, offvalue=0, variable=myval1)
cb2 = Checkbutton(myroot, image=myoff_image, selectimage=myon_image, indicatoron=False,
                     onvalue=1, offvalue=0, variable=myval2)

cb1.pack(padx=10, pady=10)
cb2.pack(padx=10, pady=10)

myroot.mainloop()
