import pen

was_pressed = False

def setup():
    global tool, img
    size(400, 400)
    tool = pen.Pen()
    img = loadImage(tool.get_icon())
    background(255)
    
    
def draw():
    global tool, img, was_pressed
    
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
