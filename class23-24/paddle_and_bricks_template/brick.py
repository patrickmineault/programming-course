class Brick:
    def __init__(self, pos_x, pos_y, w, h, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.active = True
        self.color = color
        
    def hit_test(self, x, y):
        return ((x > self.pos_x) and 
                (x < self.pos_x + self.w) and
                (y > self.pos_y) and 
                (y < self.pos_y + self.h))
        
    def draw(self):
        if self.active:
            if self.color == 'r':
                fill(255, 0, 0)
            elif self.color == 'b':
                fill(0, 0, 255)
            rect(self.pos_x, self.pos_y, self.w, self.h)
