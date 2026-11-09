from turtle import *
from superturtle.animation import *
from superturtle.movement import *
from shapes import *
import settings

colormode(255)                                  # rgb color mode
screen = Screen()
screen.setup(settings.WIDTH, settings.HEIGHT)   # sets custom screen size

bgcolor(0,0,0)              #sets background color 

for frame in animate(loop = True):

    for frame in animate(frames=settings.TOTAL_FRAMES):
        
        border_colorG = frame.interpolate(start=165, stop=255, mirror=True)
        filled_circle(100, "black", 255, int(border_colorG), 0, 10)