class Pen:
    def mouse_up(self, mouseX, mouseY):
        print("mouse up")
        
    def mouse_down(self, mouseX, mouseY):
        print("mouse down")
    
    def mouse_drag(self, pmouseX, pmouseY, mouseX, mouseY):
        line(pmouseX, pmouseY, mouseX, mouseY)
    
    def get_icon(self):
        return "pen.png"
