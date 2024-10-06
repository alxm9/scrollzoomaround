from tkinter import *
from dataclasses import dataclass
import random
from PIL import ImageTk, Image

@dataclass
class coords:
    anch_xy: list
    
cor = coords([0,0])

class program():
    def __init__(self):
        self.app = Tk()
        self.squares = {}
        self.app.geometry("500x500")
        self.interface = Canvas(self.app, bg="grey", width = 500, height = 500)      

    def start(self):
        self.binds()
        self.populate_grid()
        self.place_char()
        self.interface.pack()
        self.app.mainloop()
    
    def binds(self):
        self.app.bind("<Button-3>", lambda event: self.set_anchor(event))
        self.app.bind("<B3-Motion>", lambda event: self.move_map(event))
        self.app.bind("<x>", lambda event: print("move"))
        
    def set_anchor(self, event):
        cor.anch_xy = [event.x,event.y]
        
    def move_map(self, event):
        dx, dy = (event.x - cor.anch_xy[0]), (event.y - cor.anch_xy[1])
        for square in self.squares.values():
            self.interface.move(square,dx,dy)
        cor.anch_xy[0], cor.anch_xy[1] = (event.x), (event.y)
        
    def populate_grid(self):
        colors = ["cyan", "green", "grey"]
        for row in range(1,41):
            for col in range(1,41):
                if any(i in [1,2,3,38,39,40] for i in (row,col)):
                    color = "cyan" 
                else:
                    color = random.choice(colors)
                self.squares["{0}_{1}".format(row,col)] = self.interface.create_rectangle(-25+(25*col),-25+(25*row),0+(25*col),0+(25*row), outline = "", fill = color)
    
    def place_char(self):
        self.interface.create_image(0,0, anchor=NW, image=ImageTk.PhotoImage(Image.open(path)))
    

test = program()

test.start()