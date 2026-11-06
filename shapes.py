from turtle import *

def rounded_rectangle(width, height, color_name):
    # draws a rounded rectangle of any size and color
    
    fillcolor(color_name)
    begin_fill()
    for i in range(2):
        forward(height)
        circle(width, 180)
    end_fill()

def filled_circle(circle_size, fill_color, border_colorR, border_colorG, border_colorB, border_width):
    # draws a circle of any size, color, border color and width
    # border color RGB values can be interpolated to change shades
    colormode(255)
    pencolor(border_colorR, border_colorG, border_colorB)
    # I used geeksforgeeks to find how to use rgb values
    pensize(border_width)
    fillcolor(fill_color)
    begin_fill()
    circle(circle_size)
    end_fill()

if __name__ == "__main__":
    rounded_rectangle(10,100,"blue")
    filled_circle(100, "black", 23, 134, 12, 10)
    input()