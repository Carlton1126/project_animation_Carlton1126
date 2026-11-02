from turtle import *
from superturtle.animation import *
from superturtle.movement import *
import settings

colormode(255)                                  # rgb color mode
screen = Screen()
screen.setup(settings.WIDTH, settings.HEIGHT)   # sets custom screen size

bgcolor(settings.BACKGROUND_COLOR)              #sets background color 

for frame in animate(loop = True):

    for frame in animate(frames=settings.TOTAL_FRAMES):
        
        pass  # delete this line and write your own code!  





