import random

class SpriteSheet:
    """Manages and draws a sprite sheet.
    
    Args:
        location: the location of the sprite sheet image (png). Must be inside the data folder.
        nx: number of sprites along the x dimension.
        ny: number of sprites along the y dimension.
        
    Usage:
        ss = SpriteSheet("horse.png", 4, 2)
        ss.show()  # To draw one element of the sprite sheet.
        ss.select_next()  # To select the next sprite in the sprite sheet.
        ss.current_sprite = 3  # To select sprite 3 in the sprite sheet.
        ss.select_random()  # To select a sprite at random.
    """
    def __init__(self, location, nx, ny):
        self.location = location
        self.nx = nx
        self.ny = ny
        self.img = loadImage(location)
        self.current_sprite = 0
        self.nsprites = nx * ny 
        try:
            self.szx = self.img.width / self.nx
            self.szy = self.img.height / self.ny
        except AttributeError:
            raise Exception("The file %s does not exist. Are you sure you put it in the `data` folder?" % location)
        
    def select_random(self):
        self.current_sprite = random.randint(0, self.nsprites)
    
    def select_next(self):
        self.current_sprite += 1
        if self.current_sprite >= self.nsprites:
            self.current_sprite = 0
        
    def draw(self):
        offset_x = self.szx * (self.current_sprite % self.nx)
        offset_y = self.szy * (self.current_sprite // self.nx)
        sub_img = self.img.get(offset_x, offset_y, self.szx, self.szy)
        image(sub_img, 0, 0)
