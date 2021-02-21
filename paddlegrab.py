from powerup import PowerUp
from ball import ball

class paddlegrab(PowerUp):
    def __init__(self, x, y):
        icon="\u270A"
        super().__init__(x, y, icon)
    
    def execute(self, board):
        self.x=-1
        self.y=-1
        check_flag=0
        for pow_up in board._powerups:
            if isinstance(pow_up, paddlegrab) and pow_up.remaining_time>0:
                pow_up.remaining_time=120
                check_flag=1
        if check_flag==0:
            super().execute()
            board._paddle.stick=True
            

    def deactivate(self, board):
        super().deactivate()
        board._paddle.stick=False
        pass
