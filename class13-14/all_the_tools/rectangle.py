class Rectangle: 
    
    def mouse_down(self, mouseX, mouseY):
        self.x_beginning = mouseX
        self.y_beginning = mouseY
    
    def mouse_up(self, mouseX, mouseY):
        rect(self.x_beginning, self.y_beginning, mouseX - self.x_beginning, mouseY - self.y_beginning)
                  
    def mouse_drag(self, pmouseX, pmouseY, mouseX, mouseY):
        print("mouse drag")
    
    def get_icon(self):
        return "rectangle.png"
