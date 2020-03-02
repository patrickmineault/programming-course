import random
x = 200
y = 200

def setup():
    size(400, 400)
    global snake, apples
    snake = [0, 1]
    apples = [3, 5, 7]
    
def draw():
    global x, y
    # Once per update.
    background(0)
    stroke(255)
    fill(255)
    
    if frameCount % 30 == 0:
        head = snake[-1] + 1
        snake.append(head)
        if len(apples) > 0 and head == apples[0]:
            apples.pop(0)
        else:
            # Remove from the tail
            snake.pop(0)
        
    for segment in snake:
        rect(segment * 50, 100, 50, 50)
        
    fill(255, 255, 0)
    rect(snake[-1] * 50, 100, 50, 50)
    
        
    for apple in apples:
        fill(255, 0, 0)
        circle(50 * (apple + .5), 125, 30)
