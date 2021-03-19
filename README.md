# BRICK BREAKER
Enjoy the amazing game, where you have to use the ball and your wit to break all the bricks on the screen and get the maximum score.  
You are given a paddle on which you can bounce the ball, but if all the balls fall under that paddle, you lose your life, so be careful!!  
## Rules
### Bricks
There are 6 types of bricks:
* White - These are unbreakable, and cannot be broken any number of times you hit. These don't carry any points.
* Green - The lowest level brick. These can be destroyed in one shot. A brick initially green gives you 5 points.
* Yellow - The 2nd level brick. These can be destroyed in two shot. A brick initially yellow gives you 10 points.
* Red - The 3nd level brick. These can be destroyed in three shot. A brick initially red gives you 15 points.
* LightMagenta - The 4th level brick. These can be destroyed in four shot. A brick initially green gives you 20 points.
* Cyan - These are **explosive** bricks, which break all the bricks that are touching these bricks(horizontal/vertical/diagonal). These can even cause a chain reaction by breaking other Cyan bricks.
* Rainbow bricks - These give 20 points, and keep changing color until they are hit for the first time.
### Poweups
These powerups get the velocity of the ball. They are also accelerated by gravity while falling.  
There are 8 powerups:
* Expand Paddle - This expands the paddle by a certain length. It can be stacked to keep increasing paddle's length.
* Shrink Paddle - This shrinks the paddle by a certain length. It can be stacked to keep increasing paddle's length.
* Ball Multiplier - Doubles all the balls on the screen.
* Thru-ball - Makes the ball go FIRE, and the ball can pass through all kinds of bricks - even unbreakable ones. Getting more of these just restarts the timer of this powerup.
* Paddle Grab - Allows you to keep the ball when it falls on paddle. Getting more of these just restarts the timer of this powerup.
* Fire ball - This powerup destroys all the bricks that are adjacent to a particular brick.
* Shooting Paddle - This powerup shoots bullets continuously from the paddle and hits the bricks.
### Falling bricks
After 30 seconds, the whole brick layout keeps falling down by one block every time the ball hits the paddle. This doesn't happen in the boss level, however, since it is already difficult.
### Levels
The game consists of 4 levels, and you are redirected to next when you finish one. You can also press s key to skip the level.
### Boss Level
* This level consists of a UFO, which continuously drops bombs on the paddle and follows it.
* If a bomb hits the paddle, the paddle is destroyed, and the ball is reset on the paddle.
* The UFO tries to save itself by spawning bricks. Try to outsmart it! :) 
### Controls
* Press a to move the paddle left.
* Press d to move the paddle right.
* Press space to release the ball from paddle.
### Starting the Game
* To run the game, you need numpy and colorama. To install 
```
cd 2019114006
pip3 install numpy colorama
```
To run the game,
```
python3 main.py
```
**NOTE**: The game is made only using python and numpy(with colorama for colors). No curses or game libraries have been used.
