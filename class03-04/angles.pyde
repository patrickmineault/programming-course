import random

def setup():
    size(640, 640)
    background(0)
    noLoop()
    
def draw():
    stroke(255)
    for i in range(100):
        # Pick a length.
        length = random.random() * 100
        
        # Pick a position
        x = random.random() * width
        y = random.random() * height 
        
        # Draw it
        line(x, y, x + length, y)
        line(x, y, x, y + length)
        
    saveFrame("angles.png")
