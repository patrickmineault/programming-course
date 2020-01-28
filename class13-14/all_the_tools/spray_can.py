import random

class spraycan:
    def mouse_up(self, mouseX, mouseY):
        print("mouse up")
        
    def mouse_down(self, mouseX, mouseY):
        print("mouse down")
    
    def mouse_drag(self, pmouseX, pmouseY, mouseX, mouseY):
        for j in range(5):
            x=random.randrange(1.0,20.0)
            y=random.randrange(1.0,20.0)
            # noStroke()
            fill(0)
            circle(mouseX+x,mouseY+y,2)
        
    def get_icon(self):
        return "spraycan.png"
        
    
    
