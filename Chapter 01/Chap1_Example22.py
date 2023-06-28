from tkinter import *
myroot = Tk()

mybtn_col = Button(myroot, text="It is Column No. 4")
mybtn_col.grid(row = 0, column=4)

mybtn_colspan = Button(myroot, text="The columnspan is of 4")
mybtn_colspan.grid(row = 1,columnspan=4)

mybtn_paddingx = Button(myroot, text="padx of 5 from outside widget border")
mybtn_paddingx.grid(row = 2,padx=5)

mybtn_paddingy = Button(myroot, text="pady of 5 from outside widget border")
mybtn_paddingy.grid(row = 3,pady=5)

mybtn_ipaddingx = Button(myroot, text="ipadx of 5 from inside widget border")
mybtn_ipaddingx.grid(row = 4,ipadx=5)

mybtn_ipaddingy = Button(myroot, text="ipady of 15 from inside widget border")
mybtn_ipaddingy.grid(row = 5,ipady=15)

mybtn_row = Button(myroot, text="It is Row No. 7")
mybtn_row.grid(row=7)

mybtn_rowspan = Button(myroot, text="It is Rowspan of 3")
mybtn_rowspan.grid(row = 8,rowspan=3)

mybtn_sticky = Button(myroot, text="Hey ! I am at North-West")
mybtn_sticky.grid(sticky=NW)

myroot.mainloop()
