class Airbrush:
    def __init__(self):
        self.yellow_img = loadImage("yellowdot.png")
        self.red_img = loadImage("reddot.png")
    
    def mouse_up(self, mouseX, mouseY):
        print("mouse up")
               
    def mouse_down(self, mouseX, mouseY):
        print("mouse down")
            
    def mouse_drag(self, pmouseX, pmouseY, mouseX, mouseY):
        if mousePressed and mouseButton == LEFT :
            img = self.yellow_img
        elif mousePressed and mouseButton == RIGHT :
            img = self.red_img

        pushMatrix()
        translate(-30,-30)
        image(img, mouseX, mouseY)
        popMatrix()
    
    def get_icon(self):
        return "reddot.png"
