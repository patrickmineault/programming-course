class Ball:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 5
        
    def update(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        
    def draw(self):
        noStroke()
        fill(128, 128, 128)
        circle(self.pos_x, self.pos_y, 10)
        fill(192, 192, 192)
        circle(self.pos_x - 1, self.pos_y - 1, 2*self.radius)
