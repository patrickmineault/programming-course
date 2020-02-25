class Paddle:
    def __init__(self, pos_x, pos_y, field_size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = 40
        self.field_size = field_size
        self.circle_size = 10
        
    def update(self, target_x):
        self.pos_x = min(max(target_x, self.w / 2 + self.circle_size), self.field_size - self.circle_size - self.w / 2)
        
    def hit_test(self, x, y):
        if ((x > self.pos_x - self.w / 2 - self.circle_size / 2) and 
            (x < self.pos_x + self.w / 2 + self.circle_size / 2) and
            (y > self.pos_y - self.circle_size/2) and 
            (y < self.pos_y + 20)):
            return True
        return False
            
        
    def draw(self):
        # Draw the paddle
        stroke(0)
        pushMatrix()
        translate(self.pos_x, self.pos_y)
        fill(255, 0, 0)
        circle(-self.w // 2, 0, self.circle_size)
        circle( self.w // 2, 0, self.circle_size)
        fill(128, 128, 128)
        rect(-self.w // 2, -self.circle_size/2, self.w, self.circle_size)
        popMatrix()
