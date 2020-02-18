import scoreboard
import random

def setup():
    global sb
    sb = scoreboard.ScoreBoard() 
    sb.reset()
    size(640, 640)
    
def draw():
    global sb
    background(255)
    
    # Increase score regularly, reset at random times.
    if frameCount % 12 == 0:
        sb.score()
    if random.random() < .02:
        sb.reset()
        
    sb.draw_score()
