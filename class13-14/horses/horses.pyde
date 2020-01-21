import random
import SpriteSheet

class Horse:
    def __init__(self, y, speed):
        self.run_frames = 0
        self.x = 0
        self.y = y
        self.speed = speed
        self.ss = SpriteSheet.SpriteSheet("horse.png", 5, 3)
        self.ss.select_random()
        
    def run(self):
        self.x += self.speed
        self.run_frames += 1
        if self.run_frames % 4 == 0:
            self.ss.select_next()
        
    def draw(self):
        #circle(self.x, self.y, 25)
        pushMatrix()
        translate(self.x, self.y)
        self.ss.draw()
        popMatrix()
        
def setup():
    global horses
    size(800, 800)
    horses = []
    for i in range(6):
        horse = Horse(i * 120, random.random() * 2 + 3)
        horses.append(horse)
    
def draw():
    global horses
    background(0)
    for horse in horses:
        horse.run()
        horse.draw()
