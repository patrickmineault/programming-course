class Sticker:
    def __init__(self):
        self.photo = loadImage("doggo.png")
    
    def mouse_up(self, mouseX, mouseY):
        print("mouse up")
        
    def mouse_down(self, mouseX, mouseY):
        if mousePressed:
            image(self.photo, mouseX, mouseY, 100, 100)
        
    def mouse_drag(self, pmouseX, pmouseY, mouseX, mouseY):
        #line(pmouseX, pmouseY, mouseX, mouseY)
        print("mouse drag")
    
    def get_icon(self):
        return "doggo.png"
