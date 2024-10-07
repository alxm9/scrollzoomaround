from tkinter import *
from dataclasses import dataclass
import random

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
        self.interface.pack()
        self.populate_grid()
        # self.place_char()
        self.app.mainloop()
    
    def binds(self):
        self.app.bind("<Button-3>", lambda event: self.set_anchor(event))
        self.app.bind("<B3-Motion>", lambda event: self.move_map(event))
        self.app.bind("<Up>", lambda event: self.move(event))
        self.app.bind("<MouseWheel>", lambda event: self.zoom(event))
        self.app.bind("<Down>", lambda event: self.move(event))
        self.app.bind("<Right>", lambda event: self.move(event))
        self.app.bind("<Left>", lambda event: self.move(event))
        
    def set_anchor(self, event):
        cor.anch_xy = [event.x,event.y]
        
    def move_map(self, event):
        dx, dy = (event.x - cor.anch_xy[0]), (event.y - cor.anch_xy[1])
        for square in self.squares.values():
            self.interface.move(square,dx,dy)
        cor.anch_xy[0], cor.anch_xy[1] = (event.x), (event.y)
        
    def zoom(self, event):
        self.set_anchor(event)
        delta = {
            120: 1,
            -120: -1
        }[event.delta]
        for square in self.squares.values():
            # print(self.interface.coords(square)[0
            x0, x1, y0, y1 = self.interface.coords(square)
            print(square)
            quit()
            dx, dy = (1.2*delta)*(x - cor.anch_xy[0]), (1.2*delta)*(y - cor.anch_xy[1])
            self.interface.coords(square)[0] += dx
           
            
        
        
    def populate_grid(self):
        colors = ["cyan", "green", "green"]
        for row in range(1,41):
            for col in range(1,41):
                if any(i in [1,2,3,38,39,40] for i in (row,col)):
                    color = "cyan" 
                else:
                    color = random.choice(colors)
                self.squares["{0}_{1}".format(row,col)] = self.interface.create_rectangle(-25+(25*col),-25+(25*row),0+(25*col),0+(25*row), outline = "", fill = color)
                self.interface.tag_lower(self.squares["{0}_{1}".format(row,col)])

    def place_char(self):
        self.img = PhotoImage(file="char.png")
        self.squares["char"] = self.interface.create_image(75,75, anchor = NW,image = self.img)
        print(self.squares["char"])
    
    def move(self,event):
        keys = { 
            "Up": [0,-25],
            "Down": [0,25],
            "Left": [-25, 0],
            "Right": [25,0]
        }[event.keysym] 
        dx, dy = keys[0], keys[1]
        self.interface.move(self.squares["char"], dx,dy)

    



test = program()

# img = PhotoImage(file="char.png")
# this = test.interface.create_image(20,20,image=img)

test.start()
# test.place_char()