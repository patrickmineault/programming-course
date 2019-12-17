stroke_width = 5

def setup():
    size(400, 400)
    background(255)
    
def draw():
    global stroke_width
    
    delta = .5
    if keyPressed:
        if keyCode == DOWN:
            stroke_width = stroke_width - delta
        if keyCode == UP:
            stroke_width = stroke_width + delta
    
    if stroke_width < 1:
        stroke_width = 1
        
    print(stroke_width)
    strokeWeight(stroke_width)
    
    if mousePressed:
        if mouseButton == LEFT:
            stroke(0)
            
        if mouseButton == CENTER:
            stroke(0, 0, 255)
                        
        if mouseButton == RIGHT:
            # change stroke color to hot pink (255, 102, 189)
            stroke(255, 102, 189) 
        
        line(pmouseX, pmouseY, mouseX, mouseY)
    
