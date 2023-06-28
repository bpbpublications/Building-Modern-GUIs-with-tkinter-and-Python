from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
myroot = Tk()

myroot.geometry('600x400')
myroot.resizable(0,0)
myroot.title('Home Page')
myframe55 = None

def myscreen():
    myntb = ttk.Notebook()
    def mydemo(a1):
        print(myntb.index('current')) # getting tab positions
        if myntb.index('current') == 5:
            myhome()
    
    myntb.bind('<<NotebookTabChanged>>', mydemo)
    myntb.place(x=0,y=0,width = 600, height = 400)
    bginsertion(myntb)
    myshowall(myntb)
    mysearch(myntb)
    myupdate(myntb)
    mydelete(myntb)
    mylogout(myntb)

def bginsertion(ntb):
    myf4 = Frame(bg = 'LightBlue')
    ntb.add(myf4,text='MyInsert')
    
    m = StringVar()
    n = StringVar()
    o = StringVar()
    p = StringVar()
    q = StringVar()
    
    myl1 = Label(myf4, font = ('Calibri',15),text = 'Enter Roll No.', bg = 'LightBlue', fg = 'Red')
    myl1.place(x=150,y=50)
    mye1 = Entry(myf4, font = ('Calibri',15), textvariable = m)
    mye1.place(x = 300, y = 50, width = 100)
    
    myl2 = Label(myf4, font = ('Calibri',15),text = 'Enter Name', bg = 'LightBlue', fg = 'Red')
    myl2.place(x=150,y=100)
    mye2 = Entry(myf4, font = ('Calibri',15), textvariable = n)
    mye2.place(x = 300, y = 100, width = 100)
    
    myl3 = Label(myf4, font = ('Calibri',15),text = 'Enter Phy.', bg = 'LightBlue', fg = 'Red')
    myl3.place(x=150,y=150)
    mye3 = Entry(myf4, font = ('Calibri',15), textvariable = o)
    mye3.place(x = 300, y = 150, width = 100)
    
    myl4 = Label(myf4, font = ('Calibri',15),text = 'Enter Chem.', bg = 'LightBlue', fg = 'Red')
    myl4.place(x=150,y=200)
    mye4 = Entry(myf4, font = ('Calibri',15), textvariable = p)
    mye4.place(x = 300, y = 200, width = 100)
    
    myl5 = Label(myf4, font = ('Calibri',15),text = 'Enter Maths.', bg = 'LightBlue', fg = 'Red')
    myl5.place(x=150,y=250)
    mye5 = Entry(myf4, font = ('Calibri',15), textvariable = q)
    mye5.place(x = 300, y = 250, width = 100)
    
    def mydatainsertion():
        mydb = sqlite3.connect('mydemo.db')
        my_cursor = mydb.cursor()
        my_cursor.execute("insert into ins values('"+m.get()+"','"+n.get()+"','"+o.get()+"','"+p.get()+"','"+q.get()+"')")
        mydb.commit()
        mydb.close()
        messagebox.showinfo('Title','Data Inserted')
        m.set('')
        n.set('')
        o.set('')
        p.set('')
        q.set('')
        myshowalldata(myframe55)

    mybtn = Button(myf4, font = ('Calibri',15),text = 'Insert Data', bg = 'LightBlue', fg = 'Red', command = mydatainsertion)
    mybtn.place(x = 250, y = 300, width = 100, height = 30)

def myshowall(ntb):
    myf5 = Frame(bg = 'LightBlue')
    ntb.add(myf5,text='MyShowAll')
    global myframe55
    myframe55 = myf5
    myshowalldata(myf5)

def myshowalldata(myf5):
    # for deletion addition
    for loop in myf5.winfo_children(): # a list of all widgets are returned
        loop.destroy()
    
    myu1 = Label(myf5, font = ('Arial',12), text = 'Roll No.',bg = 'LightBlue', fg = 'Red')
    myu1.place(x=0,y=0, width = 120)
    
    myu2 = Label(myf5, font = ('Arial',12), text = 'Name',bg = 'LightBlue', fg = 'Red')
    myu2.place(x=120,y=0, width = 120)
    
    myu3 = Label(myf5, font = ('Arial',12), text = 'Phy.',bg = 'LightBlue', fg = 'Red')
    myu3.place(x=240,y=0, width = 120)
    
    myu4 = Label(myf5, font = ('Arial',12), text = 'Chem.',bg = 'LightBlue', fg = 'Red')
    myu4.place(x=360,y=0, width = 120)
    
    myu5 = Label(myf5, font = ('Arial',12), text = 'Maths',bg = 'LightBlue', fg = 'Red')
    myu5.place(x=480,y=0, width = 120)
    
    db = sqlite3.connect('mydemo.db')
    cr = db.cursor()
    r = cr.execute("select * from ins ")
    x = 50
    y = 60
    for loop in r:
        Label(myf5,text = loop[0], font = ('Arial',12),bg = 'LightBlue', fg = 'Red').place(x=x,y=y)
        x += 120
        Label(myf5,text = loop[1], font = ('Arial',12),bg = 'LightBlue', fg = 'Red').place(x=x,y=y)
        x += 120
        Label(myf5,text = loop[2], font = ('Arial',12),bg = 'LightBlue', fg = 'Red').place(x=x,y=y)
        x += 120
        Label(myf5,text = loop[3], font = ('Arial',12),bg = 'LightBlue', fg = 'Red').place(x=x,y=y)
        x += 120
        Label(myf5,text = loop[4], font = ('Arial',12),bg = 'LightBlue', fg = 'Red').place(x=x,y=y)
        y += 60
        x = 50

def mysearch(ntb):
    myf6 = Frame(bg = 'LightBlue')
    ntb.add(myf6,text='MySearch')
    
    s1 = StringVar()
    
    myu1 = Label(myf6, font = ('Arial',12), text = 'Roll No.',bg = 'LightBlue', fg = 'Red')
    myu1.place(x=100,y=50, width = 120)
    
    mye1 = Entry(myf6, font = ('Calibri',15), textvariable = s1)
    mye1.place(x = 200, y = 50, width = 100)
    
    def searched():
        db = sqlite3.connect('mydemo.db')
        cr = db.cursor()
        r = cr.execute("select * from ins where URNO ='"+s1.get()+"' ")
        for loop in r:
            myl1 = Label(myf6, text = "Name is: ", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl1.place(x=200,y=100)
            
            myl2 = Label(myf6, text = loop[1], font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl2.place(x=350,y=100)
            
            myl1 = Label(myf6, text = "Phy : ", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl1.place(x=200,y=150)
            
            myl2 = Label(myf6, text = loop[2], font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl2.place(x=350,y=150)
            
            myl1 = Label(myf6, text = "Chem : ", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl1.place(x=200,y=200)
            
            myl2 = Label(myf6, text = loop[3], font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl2.place(x=350,y=200)
            
            myl1 = Label(myf6, text = "Maths : ", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl1.place(x=200,y=250)
            
            myl2 = Label(myf6, text = loop[4], font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl2.place(x=350,y=250)

            break
        else:
            messagebox.showinfo('Title','Roll No. absent')
            myl11 = Label(myf6, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl11.place(x=200,y=100,width=300)
            
            myl12 = Label(myf6, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl12.place(x=350,y=100,width=300)
            
            myl13 = Label(myf6, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl13.place(x=200,y=150,width=300)
            
            myl14 = Label(myf6, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl14.place(x=350,y=150,width=300)
            
            myl15 = Label(myf6, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl15.place(x=200,y=200,width=300)
            
            myl16 = Label(myf6, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl16.place(x=350,y=200,width=300)
            
            myl17 = Label(myf6, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl17.place(x=200,y=250,width=300)
            
            myl18 = Label(myf6, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl18.place(x=350,y=250)

        db.commit()
        db.close()
    
    mybtn = Button(myf6, text = 'Search', font = ('Calibri',15), command = searched)
    mybtn.place(x=320,y=50, width = 100,height = 30)

def myupdate(ntb):
    myf7 = Frame(bg = 'LightBlue')
    ntb.add(myf7,text='MyUpdate')
    
    s2 = StringVar()
    
    myu1 = Label(myf7, font = ('Arial',12), text = 'Roll No.',bg = 'LightBlue', fg = 'Red')
    myu1.place(x=100,y=50, width = 120)
    
    mye1 = Entry(myf7, font = ('Calibri',15), textvariable = s2)
    mye1.place(x = 200, y = 50, width = 100)
    
    def updated():
        db = sqlite3.connect('mydemo.db')
        cr = db.cursor()
        r = cr.execute("select * from ins where URNO ='"+s2.get()+"' ")
        for loop in r:
            s3 = StringVar()
            s4 = StringVar()
            s5 = StringVar()
            s6 = StringVar()
            
            myl1 = Label(myf7, text = "Name is: ", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl1.place(x=200,y=100)

            myl2 = Entry(myf7, font = ('Calibri',15), bg = 'LightBlue', fg = 'Red', textvariable = s3)
            myl2.insert(0,loop[1])
            myl2.place(x=350,y=100)

            myl1 = Label(myf7, text = "Phy : ", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl1.place(x=200,y=150)
            
            myl2 = Entry(myf7, font = ('Calibri',15), bg = 'LightBlue', fg = 'Red', textvariable = s4)
            myl2.insert(0,loop[2])
            myl2.place(x=350,y=150)
            
            myl1 = Label(myf7, text = "Chem : ", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl1.place(x=200,y=200)
            
            myl2 = Entry(myf7, font = ('Calibri',15), bg = 'LightBlue', fg = 'Red', textvariable = s5)
            myl2.insert(0,loop[3])
            myl2.place(x=350,y=200)
            
            myl1 = Label(myf7, text = "Maths : ", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl1.place(x=200,y=250)
            
            myl2 = Entry(myf7, font = ('Calibri',15), bg = 'LightBlue', fg = 'Red', textvariable = s6)
            myl2.insert(0,loop[4])
            myl2.place(x=350,y=250)
            
            def updatedata2():
                mydb = sqlite3.connect('mydemo.db')
                my_cursor = mydb.cursor()
                my_cursor.execute("update ins set UNAME = '"+s3.get()+"',UPHY ='"+s4.get()+"',UCHE ='"+s5.get()+"',UMATHS ='"+s6.get()+"' WHERE URNO ='"+s2.get()+"' ")
                mydb.commit()
                mydb.close()
                messagebox.showinfo('Title','Data Updated')
                s3.set('')
                s4.set('')
                s5.set('')
                s6.set('')
                myshowalldata(myframe55)
            
            mybtn = Button(myf7, text = 'Update', font = ('Calibri',15), command = updatedata2)
            mybtn.place(x=250,y=325, width = 100,height = 30)

            break
        else:
            messagebox.showinfo('Title','Roll No. absent')
            myl11 = Label(myf7, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl11.place(x=200,y=100,width=300)
            
            myl12 = Label(myf7, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl12.place(x=350,y=100,width=300)
            
            myl13 = Label(myf7, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl13.place(x=200,y=150,width=300)
            
            myl14 = Label(myf7, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl14.place(x=350,y=150,width=300)
            
            myl15 = Label(myf7, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl15.place(x=200,y=200,width=300)
            
            myl16 = Label(myf7, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl16.place(x=350,y=200,width=300)
            
            myl17 = Label(myf7, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl17.place(x=200,y=250,width=300)
            
            myl18 = Label(myf7, text = "", font = ('Calibri',15), bg = 'LightBlue', fg = 'Red')
            myl18.place(x=350,y=250)

        db.commit()
        db.close()
    
    mybtn = Button(myf7, text = 'Retrieve', font = ('Calibri',15), command = updated)
    mybtn.place(x=320,y=50, width = 100,height = 30)
    
def mydelete(ntb):
    myf8 = Frame(bg = 'LightBlue')
    ntb.add(myf8,text='MyDelete')
    
    s1 = StringVar()
    
    myu1 = Label(myf8, font = ('Arial',12), text = 'Roll No.',bg = 'LightBlue', fg = 'Red')
    myu1.place(x=100,y=50, width = 120)
    
    mye1 = Entry(myf8, font = ('Calibri',15), textvariable = s1)
    mye1.place(x = 200, y = 50, width = 100)
    
    def mydeletion():
        db = sqlite3.connect('mydemo.db')

        cr = db.cursor()
        r = cr.execute("delete from ins where URNO ='"+s1.get()+"'  ")
        messagebox.showinfo('Title','Data deleted')
        db.commit()
        db.close()
        myshowalldata(myframe55)
        s1.set('')
    
    mybtn = Button(myf8, text = 'Delete', font = ('Calibri',15), command = mydeletion)
    mybtn.place(x=320,y=50, width = 100,height = 30)

def mylogout(ntb):
    myf9 = Frame(bg = 'LightBlue')
    ntb.add(myf9,text='MyLogOut')

def mylogin():
    myf2 = Frame(bg = 'LightBlue')
    myf2.place(x=0,y=0, width = 600, height = 400)
    
    d = StringVar()
    e = StringVar()
    
    myl1 = Label(myf2, text = 'Enter Name: ', bg = 'LightBlue', fg = 'Red')
    myl1.place(x=200,y=100)
    mye1 = Entry(myf2, font = ('Calibri',15), textvariable = d)
    mye1.place(x = 300, y =100, width = 100, height = 20)
    
    myl2 = Label(myf2, text = 'Enter Password: ', bg = 'LightBlue', fg = 'Red')
    myl2.place(x=200,y=150)
    mye2 = Entry(myf2, font = ('Calibri',15), textvariable = e)
    mye2.place(x = 300, y =150, width = 100, height = 20)
    
    def login1():
        db = sqlite3.connect('mydemo.db')
        cr = db.cursor()
        r = cr.execute("select * from regis where UNAME ='"+d.get()+"' AND UPASS ='"+e.get()+"' ")
        for loop in r:
            myscreen()
            break
        else:
            messagebox.showinfo('Title','Invalid user name and password')
        db.commit()
        db.close()
    
    mybtn = Button(myf2, text = 'Login', font = ('Calibri',15), command = login1)
    mybtn.place(x=250,y=200, width = 100,height = 30)
    
    mybtn1 = Button(myf2, text = 'Home', font = ('Calibri',15), command = myhome)
    mybtn1.place(x=20,y=350, width = 100,height = 30)
    
    mybtn2 = Button(myf2, text = 'Registration', font = ('Calibri',15), command = myregis)
    mybtn2.place(x=480,y=350, width = 120,height = 30)

def myregis():
    myf2 = Frame(bg = 'LightBlue')
    myf2.place(x=0,y=0, width = 600, height = 400)
    
    a = StringVar()
    b = StringVar()
    c = StringVar()
    
    myl1 = Label(myf2, text = 'Enter Name: ', bg = 'LightBlue', fg = 'Red')
    myl1.place(x=200,y=100)
    mye1 = Entry(myf2, font = ('Calibri',15), textvariable = a)
    mye1.place(x = 300, y =100, width = 100, height = 20)
    
    myl2 = Label(myf2, text = 'Enter Password: ', bg = 'LightBlue', fg = 'Red')
    myl2.place(x=200,y=150)
    mye2 = Entry(myf2, font = ('Calibri',15), textvariable = b)
    mye2.place(x = 300, y =150, width = 100, height = 20)
    
    myl3 = Label(myf2, text = 'Enter CN: ', bg = 'LightBlue', fg = 'Red')
    myl3.place(x=200,y=200)
    mye3 = Entry(myf2, font = ('Calibri',15), textvariable = c)
    mye3.place(x = 300, y =200, width = 100, height = 20)
    
    def registring():
        mydb = sqlite3.connect('mydemo.db')
        my_cursor = mydb.cursor()
        my_cursor.execute("insert into regis values('"+a.get()+"','"+b.get()+"','"+c.get()+"')")
        mydb.commit()
        mydb.close()
        messagebox.showinfo('Title','User Registered')
        a.set('')
        b.set('')
        c.set('')
    
    mybtn = Button(myf2, text = 'Register', font = ('Calibri',15), command = registring)
    mybtn.place(x=250,y=250, width = 120,height = 30)
    
    mybtn1 = Button(myf2, text = 'Home', font = ('Calibri',15), command = myhome)
    mybtn1.place(x=20,y=350, width = 100,height = 30)
    
    mybtn2 = Button(myf2, text = 'Login', font = ('Calibri',15), command = mylogin)
    mybtn2.place(x=480,y=350, width = 120,height = 30)

def myhome():
    myf1 = Frame(bg = 'LightBlue')
    myf1.place(x=0,y=0, width = 600, height = 400)
    
    myb1 = Button(myf1, text = 'Login', command = mylogin)
    myb1.place(x=220,y=100,width = 100, height = 30)
    
    myb2 = Button(myf1, text = 'Register', command = myregis)
    myb2.place(x=330,y=100,width = 100, height = 30)
    
myhome()
myroot.mainloop()
