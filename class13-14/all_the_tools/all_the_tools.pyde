import airbrush
import pen
import spray_can
import sticker
import rectangle
import random

was_pressed = False

def setup():
    global tool, tools, img, imgs
    size(400, 400)
    tools = [pen.Pen(), spray_can.spraycan(), 
             rectangle.Rectangle(), sticker.Sticker(), 
             airbrush.Airbrush()]
    
    imgs = []
    for i in range(len(tools)):
        im = loadImage(tools[i].get_icon())
        try:
            im.width
        except AttributeError:
            raise Exception("File %s doesn't exist" % tools[i].get_icon())
        imgs.append(im)
    
    tool = tools[0]
    img = imgs[0]
    
    background(255)
    
def draw():
    global tool, tools, img, imgs, was_pressed
    
    
    
    if keyPressed:
        if key == 'a':
            tool = tools[0]
            img = imgs[0]
        elif key == 's':
            tool = tools[1]
            img = imgs[1]
        elif key == 'd':
            tool = tools[2]
            img = imgs[2]
        elif key == 'f':
            tool = tools[3]
            img = imgs[3]
        elif key == 'g':
            tool = tools[4]
            img = imgs[4]
        elif key == 'r':
            fill(random.random() * 255,random.random() * 255, random.random() * 255)
        elif key == 't':
            stroke(random.random() * 255,random.random() * 255, random.random() * 255)
    
    rect(0, 0, 32, 32)
    image(img, 0, 0, 32, 32)
    
    if not was_pressed and mousePressed:
        tool.mouse_down(mouseX, mouseY)
        was_pressed = True
        
    
    if mousePressed:
        tool.mouse_drag(pmouseX, pmouseY, mouseX, mouseY)

    if not mousePressed and was_pressed:
        tool.mouse_up(mouseX, mouseY) 
        was_pressed = False
