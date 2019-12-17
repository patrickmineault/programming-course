x = 200
y = 200

def setup():
    size(400, 400)
    background(128)
    
def draw():
    global x, y
    
    px = x
    py = y
    
    if keyPressed:
        if keyCode == DOWN:
            y = y + 10
        if keyCode == UP:
            y = y - 10
        if keyCode == LEFT:
            x = x - 10
        if keyCode == RIGHT:
            x = x + 10
            
        if key == " ":
            background(128)
            
    line(x, y, px, py)        
