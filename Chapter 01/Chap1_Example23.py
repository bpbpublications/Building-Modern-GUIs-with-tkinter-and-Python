from tkinter import *
myroot = Tk()
myroot.geometry("600x600")

mybtn_height = Button(myroot, text="60px high")
mybtn_height.place(height=60, x=300, y=300)

mybtn_width = Button(myroot, text="70px wide")
mybtn_width.place(width=70, x=400, y=400)

mybtn_relheight = Button(myroot, text="relheight of 0.7")
mybtn_relheight.place(relheight=0.7)

mybtn_relwidth= Button(myroot, text="relwidth of 0.4")
mybtn_relwidth.place(relwidth=0.4)

mybtn_relx=Button(myroot, text="relx of 0.5")
mybtn_relx.place(relx=0.5)

mybtn_rely=Button(myroot, text="rely of 0.8")
mybtn_rely.place(rely=0.8)

mybtn_x=Button(myroot, text="X = 500px")
mybtn_x.place(x=500)

mybtn_y=Button(myroot, text="Y = 520")
mybtn_y.place(y=520)

myroot.mainloop()
