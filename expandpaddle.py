from powerup import PowerUp

class expandpaddle(PowerUp):
    def __init__(self, x, y):
        icon="\u2795"
        super().__init__(x, y, icon)
    
    def execute(self, board):
        super().execute()
        board._paddle.increasesize()
    
    def deactivate(self, board):
        super().deactivate()
        board._paddle.decreasesize()
