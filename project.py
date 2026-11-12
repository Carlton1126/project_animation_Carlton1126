from turtle import *
from superturtle.animation import *
from superturtle.movement import *
from shapes import *
import settings

colormode(255)                                  # rgb color mode
screen = Screen()
screen.setup(settings.WIDTH, settings.HEIGHT)   # sets custom screen size



for frame in animate(loop = True):

    for frame in animate(frames=settings.TOTAL_FRAMES):

        bg = frame.interpolate(start=0, stop=255, mirror=False, easing=easeInExpo)
        screen.bgcolor(int(bg), int(bg), int(bg))
        # Makes the background go from black to white slowly
        
        with frame.scale(start=1, stop=10, first_frame=0, easing=easeInExpo):
            border_colorG = frame.interpolate(start=165, stop=255, mirror=True)
            # Makes the border of the black hole interpolate between yellow and orange
            filled_circle(100, "black", 255, int(border_colorG), 0, 10)

        
