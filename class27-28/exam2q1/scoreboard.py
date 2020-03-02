class MyPointSystem:
    def __init__(self):
        # Initialize the state of our point system
        self.reset()
        self.reset_max_score()
    
    def reset_max_score(self):
        self.max_score = 0
    
    def reset(self):
        self.current_score = 0
        
    def score(self):
        self.current_score += 1
        if self.current_score > self.max_score:
            self.max_score = self.current_score
            
    def draw_score(self):
        print("Inside draw_score")
        print(self.current_score, self.max_score)
        fill(0)
        textSize(50)
        textAlign(LEFT)
        text(self.current_score, 20, 100)
        
        textAlign(RIGHT)
        text(self.max_score, width - 20, 100)
        
        textSize(20)
        textAlign(CENTER)
        line(width / 2, 0, width/2, height)
        text("SCOREBOARD", width/2.0, 20)
        
        
