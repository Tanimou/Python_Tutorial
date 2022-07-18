class Ball():
    def __init__(self,canvas,x,y,diameter,xvelocity,yvelocity,color):
        self.canvas =canvas 
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color) 
        self.xvelocity=xvelocity
        self.yvelocity=yvelocity
    
    def move(self):
        coordinates=self.canvas.coords(self.image)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xvelocity=-self.xvelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yvelocity=-self.yvelocity
        self.canvas.move(self.image,self.xvelocity,self.yvelocity)
        




