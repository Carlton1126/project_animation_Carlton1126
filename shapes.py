from turtle import *

def triangle(size,color_name):
    # draws a triangle of any size and color
    color(color_name)
    begin_fill()
    for i in range(3):
        forward(size)
        left(120)
    # left(60)
    end_fill()

def rectangle(width, height, color_name):
    # draws a rectangle of any size and color
    color(color_name)
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def filled_circle(circle_size, color_name):
    # draws a circle of any size and color
    pencolor(color_name)
    fillcolor(color_name)
    begin_fill()
    circle(circle_size)
    end_fill()

if __name__ == "__main__":
    triangle(100, 'red')
    input()