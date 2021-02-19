class paddle:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.length=20
        self.actual_length=20
        self.stick=False
    
    def movepaddle(self, key):
        if key=='d':
            self.y+=3
        elif key=='a':
            self.y-=3
    
    def increasesize(self):
        self.actual_length+=6
        self.length=max(self.actual_length,2)
    
    def decreasesize(self):
        self.actual_length-=6
        self.length=max(self.actual_length,2)
