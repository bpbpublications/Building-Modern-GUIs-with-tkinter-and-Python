from tkinter import *
 
class CreatePolygon(Frame):
    def __init__(self, myroot=None):
        # myroot object is initialised 
        super().__init__(myroot) # Calling Frame.__init__(myroot)
        self.myroot = myroot # Update the myroot object after Frame() makes necessary changes to it
        
    def mycreateCanvas(self, mycanvas_width, mycanvas_height):
        # Creating  canvas object
        mycanvas = Canvas(self.myroot, bg="LightBlue", width=mycanvas_width, height=mycanvas_height)
        return mycanvas
    
    def mycreate_polygon(self, mycanvas):
        mypoints = [100,200,200,100,250,350,100,200]
        mycanvas.create_polygon(mypoints,fill = 'Yellow', outline = 'Red', width = 2) # polygon creation
        return mycanvas
 
# Create our myroot object to the Application
myroot = Tk()
myroot.title('polygoncreation')

# Creating create_polygon object
myobj = CreatePolygon(myroot=myroot)
mycanvas = myobj.mycreateCanvas(400, 400)
mycanvas = myobj.mycreate_polygon(mycanvas)

# The items are packed into the canvas
mycanvas.pack()
# Start the mainloop
myobj.mainloop()
