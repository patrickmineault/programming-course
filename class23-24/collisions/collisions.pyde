class Ball:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 25
    
    def hit_test(self, x, y):
        # Returns true if the coordinate x, y is within the ball.
        return (self.pos_x - x) ** 2 + (self.pos_y - y) ** 2 < self.radius ** 2
    
    def update(self):
        # updates the position of the ball according to game physics.
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
    
    def draw(self):
        # Draws the ball on the screen
        circle(self.pos_x, self.pos_y, 2*self.radius)
        
class Brick:
    def __init__(self, pos_x, pos_y, w, h):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.active = True
    
    def hit_test(self, x, y):
        # Returns true if the coordinate x, y is within the brick.
        return (x > self.pos_x and x < (self.pos_x + self.w) and
                y > self.pos_y and y < (self.pos_y + self.h))  
    
    def draw(self):
        # Draws the brick on the screen
        if self.active:
            rect(self.pos_x, self.pos_y, self.w, self.h)
        
def setup():
    global bricks, ball
    ball = Ball(155, 150)
    ball.speed_x = 5
    ball.speed_y = -5
    
    bricks = []
    for i in range(5):
        brick = Brick(100 * i, 0, 100, 30)
        bricks.append(brick) 
        brick = Brick(100 * i, 400, 100, 30)
        bricks.append(brick)
    size(500, 500)
    
    
def draw():
    global bricks, ball
    background(0)
    ball.update()
    
    for brick in bricks:
        if brick.active:
            # Collision detection type 1:
            # Bottom hit detection
            if brick.hit_test(ball.pos_x, ball.pos_y - ball.radius):
                brick.active = False
                ball.speed_y = -ball.speed_y
                continue
            
            # Now test the other parts of the ball
                     
            # Collision detection type 2:
            # Bottom right corner
            if ball.hit_test(brick.pos_x + brick.w, brick.pos_y + brick.h):
                brick.active = False
                ball.speed_x, ball.speed_y = -ball.speed_y, -ball.speed_x
                continue
            
            # Now test other corners of the brick
    
    # Bounce around the playfield
    if (ball.pos_x + ball.radius > width or 
        ball.pos_x - ball.radius < 0):
        ball.speed_x = -ball.speed_x
    
    if (ball.pos_y + ball.radius > height or 
        ball.pos_y - ball.radius < 0):
        ball.speed_y = -ball.speed_y
            
    # Finally, draw all the bricks
    for brick in bricks:
        brick.draw()
        
    ball.draw()
