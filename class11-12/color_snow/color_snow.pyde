import random

def setup():
    global star_x, star_y, shade
    star_x = []
    star_y = []
    shade = []
    colorMode(HSB, 360, 100, 100)
    for i in range(100):
        star_x.append(400 * random.random())
        star_y.append(400 * random.random())
        shade.append(random.random() * 360)
    size(400, 400)
    
def draw():
    global star_x, star_y, shade, down_to_zero
    background(128)
    for i in range(len(star_x)):
        the_color = color(shade[i], 100, 100)
        fill(the_color)
        star_y[i] += 1 + random.random() * 2
        if star_y[i] > width:
            star_y[i] = 0
            star_x[i] = random.random() * height
        circle(star_x[i], star_y[i], 30)
