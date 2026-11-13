from turtle import *
from superturtle.animation import *
from superturtle.movement import *
from superturtle.easing import easeInExpo, easeOutExpo
from shapes import *
import settings

colormode(255)                                  # rgb color mode
screen = Screen()
screen.setup(settings.WIDTH, settings.HEIGHT)   # sets custom screen size



for frame in animate(loop = True):

    for frame in animate(frames=settings.TOTAL_FRAMES):
        
        with frame.translate(start=[172, 319], stop=[0, 0]):
            filled_circle(5, "blue", 0, 0, 0, 1)
        with frame.translate(start=[-393, 305], stop=[0, 0]):
            filled_circle(5, "purple", 0, 0, 0, 1)
        with frame.translate(start=[-333, -398], stop=[0, 0]):
            filled_circle(5, "lime", 0, 0, 0, 1)
        with frame.translate(start=[212, -156], stop=[0, 0]):
            filled_circle(5, "green", 0, 0, 0, 1)
        with frame.translate(start=[158, 378], stop=[0, 0]):
            filled_circle(5, "red", 0, 0, 0, 1)
        with frame.translate(start=[-386, 320], stop=[0, 0]):
            filled_circle(5, "brown", 0, 0, 0, 1)
        with frame.translate(start=[-260, -381], stop=[0, 0]):
            filled_circle(5, "yellow", 0, 0, 0, 1)
        with frame.translate(start=[272, -121], stop=[0, 0]):
            filled_circle(5, "navy blue", 0, 0, 0, 1)
        with frame.translate(start=[156, 170], stop=[0, 0]):
            filled_circle(5, "green", 0, 0, 0, 1)
        with frame.translate(start=[-264, 190], stop=[0, 0]):
            filled_circle(5, "blue", 0, 0, 0, 1)
        # Makes the planets&moves them towards the center into the black hole
        
        with frame.scale(start=1, stop=10, first_frame=0, easing=easeInExpo):
            border_colorG = frame.interpolate(start=165, stop=255, mirror=True)
            # Makes the border of the black hole interpolate between yellow and orange
            filled_circle(100, "black", 255, int(border_colorG), 0, 10)

        bg = frame.interpolate(start=0, stop=255, mirror=False)
        screen.bgcolor(int(bg), int(bg), int(bg))
        # Makes the background go from black to white slowly