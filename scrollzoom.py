from tkinter import *
from dataclasses import dataclass
import random
from timeit import default_timer as timer
from multiprocessing import Pool

@dataclass
class coords:
    anch_xy: list
    
cor = coords([0,0])

def zoom_pool(cor_list):
    square,x0,y0,x1,y1,delta = cor_list[0],cor_list[1][0], cor_list[1][1], cor_list[1][2], cor_list[1][3], cor_list[2]
    x0 += (0.25*delta)*(x0 - cor.anch_xy[0])
    x1 += (0.25*delta)*(x1 - cor.anch_xy[0])
    y0 += (0.25*delta)*(y0 - cor.anch_xy[1])
    y1 += (0.25*delta)*(y1 - cor.anch_xy[1])
    return (square,x0,y0,x1,y1)

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
        self.app.bind("<Button-4>", lambda event: self.zoom(event))
        self.app.bind("<Button-5>", lambda event: self.zoom(event))
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
        start = timer()
        self.set_anchor(event)
        # print(event)
        delta = {
            4: 1,
            5: -1
        }[event.num]
        with Pool(5) as workers:
            # for square in self.squares.values():
                # print("THIS IS IT: ", self.interface.coords(square))
            results = workers.map(zoom_pool, [(square,self.interface.coords(square),delta) for square in self.squares.values()] )
        for result in results:
            self.interface.coords(*result)
        # print(delta)
        # for square in self.squares.values():
            # x0, y0, x1, y1 = self.interface.coords(square)
            # x0 += (0.25*delta)*(x0 - cor.anch_xy[0])
            # x1 += (0.25*delta)*(x1 - cor.anch_xy[0])
            # y0 += (0.25*delta)*(y0 - cor.anch_xy[1])
            # y1 += (0.25*delta)*(y1 - cor.anch_xy[1])
            # self.interface.coords(square, x0, y0, x1, y1)
        end = timer()
        print(end - start)
           
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
