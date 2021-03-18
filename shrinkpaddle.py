from powerup import PowerUp

class shrinkpaddle(PowerUp):
    def __init__(self, x, y, x_vel, y_vel):
        icon="\u2796"
        super().__init__(x, y, x_vel, y_vel, icon)
    
    def execute(self, board):
        super().execute()
        board._paddle.decreasesize()

    def deactivate(self, board):
        super().deactivate()
        board._paddle.increasesize()
