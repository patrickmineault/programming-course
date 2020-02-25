from brick import Brick
from ball import Ball
from paddle import Paddle

marginX = 10
marginY = 16
mode = 'mouse'
dragging = True
nballs_initial = 3
game_state = 'frozen'
state_start_time = 0

def reset_game():
    global game_over, nballs, dragging, bricks
    game_over = False
    nballs = nballs_initial
    dragging = True
    for brick in bricks:
        brick.active = True

def create_brick_layout():
    # Read a level from disk and draw it as a pattern of bricks.
    bricks = []
    lines = []
    f = open('files/level.txt')
    for line in f.readlines():
        lines.append(line)
    f.close()
    
    nbricks_wide = len(lines[0]) - 1
    nbricks_high = len(lines)
    
    brick_width = (width - 2 * marginX) / nbricks_wide
    brick_height = brick_width / 2 
    
    for j in range(nbricks_high):
        for i in range(nbricks_wide):
            color = lines[j][i]
            if color != ' ':
                bricks.append(Brick(i * brick_width, j * brick_height, brick_width, brick_height, color))
     
    # For debugging purposes, make one big brick.        
    #bricks = [Brick(0, 0, width - 2 * marginX, 100, 'r')]
    return bricks
    
def setup():
    global bricks, the_ball, score_balls, paddle
    size(400, 400)
    
    pos_x = 0
    pos_y = height - 40
    bricks = create_brick_layout()
    
    # Use the Ball class to draw some balls on the score board (trick!).
    score_balls = []
    for i in range(nballs_initial):
        score_balls.append(Ball(i * 10 + 10, 8))
    
    paddle = Paddle(pos_x, pos_y, width - marginX * 2)
    the_ball = Ball(pos_x, pos_y - 20)
    
    reset_game()
    frameRate(60)

def draw():
    global game_state, state_start_time, elapsed_time
    new_state = 'null'
    if game_state == 'playing':
        new_state = play_game(True)
    elif game_state == 'frozen':
        new_state = play_game(False)
    elif game_state == 'won' or game_state == 'lost':
        new_state = display_game_over(game_state, elapsed_time)
    
    if new_state and new_state != game_state:
        game_state = new_state
        elapsed_time = millis() - state_start_time
        state_start_time = millis()
        
    if game_state == 'frozen' and (millis() - state_start_time) > 500:
        # Unfreeze after 500 milliseconds.
        game_state = 'playing'
        elapsed_time = millis() - state_start_time
        state_start_time = millis()
        
def play_game(process_inputs):
    global bricks, dragging, the_ball, score_balls, nballs, the_ball, paddle, mode
    
    background(0)
    # Draw the background frame
    fill(128)
    rect(0, marginY, width, height - marginY)
    noStroke()
    fill(0, 0, 64)
    rect(marginX, marginY, width - 2*marginX, height)
    stroke(255)
    line(0, marginY, width, marginY)

    circle_size = the_ball.radius
    field_size = width - 2*marginX
    
    pos_x = paddle.pos_x
    oldpos_x = paddle.pos_x
    
    if process_inputs:
        # Process input
        if pmouseX != mouseX or pmouseY != mouseY:
            mode = 'mouse'
            
        if keyPressed:
            mode = 'keyboard'
        
        if mode == 'mouse':
            pos_x = mouseX - marginX
            if mousePressed and dragging:
                the_ball.speed_x = 5
                the_ball.speed_y = -5
                dragging = False
            
        if mode == 'keyboard':
            if keyPressed and keyCode == LEFT:
                pos_x -= 10
            if keyPressed and keyCode == RIGHT:
                pos_x += 10
            if keyPressed and key == ' ' and dragging:
                the_ball.speed_x = 5
                the_ball.speed_y = -5
                dragging = False                

    paddle.update(pos_x)

    if dragging:
        the_ball.pos_x = paddle.pos_x
        the_ball.pos_y = paddle.pos_y - 10
        
    the_ball.update()
    
    paddle_speed = (paddle.pos_x - oldpos_x)
    
    # Bounce the balls off the walls.
    if the_ball.pos_x > width - 2 * marginX - the_ball.radius or the_ball.pos_x < the_ball.radius:
        the_ball.speed_x = -the_ball.speed_x
  
    if the_ball.pos_y < 15:
        the_ball.speed_y = -the_ball.speed_y
    
    # Paddle hit detection.
    if the_ball.speed_y > 0 and paddle.hit_test(the_ball.pos_x, the_ball.pos_y + the_ball.radius):
        print("Collided!")
        # Check for collision
        the_ball.speed_y = - the_ball.speed_y
        
        # add momentum transfer
        the_ball.speed_x -= .2 * paddle_speed        

    if the_ball.pos_y + 10 >= paddle.pos_y + 30:
        # Remove one ball from play
        dragging = True
        nballs -= 1

    # Draw the bricks, paddle and balls (in that order!).
    pushMatrix()
    translate(marginX, 20)
    score = 0
    ndown = 0
    for j in range(len(bricks)):
        if bricks[j].hit_test(the_ball.pos_x, the_ball.pos_y):
            bricks[j].active = False
            
        bricks[j].draw()
        if not bricks[j].active:
            ndown += 1
            if bricks[j].color == 'r':
                score += 200
            else:
                score += 100
                
    paddle.draw()
    the_ball.draw()
    
    popMatrix()
    
    # Draw some around the score board.
    for i in range(nballs):
        score_balls[i].draw()

    # Draw the score.
    fill(255)
    textAlign(RIGHT)
    text("%d" % score, width - 10, 12)
    
    if ndown == len(bricks):
        # won!
        return 'won'
        
    if nballs <= 0:
        return 'lost'
    
def display_game_over(win_state, elapsed_time):
    global bricks
    textAlign(CENTER)
    fill(255)
    if win_state == 'lost':
        text("Game over :(\n\nClick to continue", width / 2, height/2)
    elif win_state == 'won':
        text("You won in %.1fs!\n\nYou cleared %.1f bricks/seconds" % (elapsed_time / 1000.0, elapsed_time / float(len(bricks)) / 1000.0), 
            width/2, height/2)
    
    # Restart the game.
    if mousePressed:
        reset_game()
        return 'frozen'
