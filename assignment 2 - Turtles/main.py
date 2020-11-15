'''
Project Name: Jack-O-Lantern Face
Author: Jonathon Carr
Due Date 10/3/2020
Course: CS-1400-007

I learned alot about using a turtle to draw stuff. I originally put the begin/end fill functions inside my loops and it
didn't work. The problem was that the computer saw my shape as just lines inside of my loop whereas outside of the loop
it saw the whole shape. When I put the fill functions outside of the loop it worked perfectly.
'''
import turtle
import time

def draw_rectangle(fillColor, lengthSide1, lengthSide2):
    turtle.fillcolor(fillColor)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(lengthSide1)
        turtle.right(90)
        turtle.forward(lengthSide2)
        turtle.right(90)
    turtle.end_fill()


def draw_triangle(fillColor, lengthOfEachSide):
    turtle.fillcolor(fillColor)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(lengthOfEachSide)
        turtle.left(120)
    turtle.end_fill()

def jack_o_lantern(width , height):

    if width < 1 or height < 1:
        print("Enter postive integers for width and height.")
        return

    # set up drawing settings
    turtle.screensize(width , height)
    turtle.bgcolor("orange")
    turtle.color("black" , "red")
    turtle.pensize(5)

    # draw first triangle
    draw_triangle("khaki", 100)

    # draw second triangle
    turtle.left(110)
    draw_triangle("gold", 120)

    #Setup for rectangle
    turtle.penup()
    turtle.right(210)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(120)
    turtle.right(180)
    turtle.pendown()
    draw_rectangle("yellow", 200, 50)

    time.sleep(20)

jack_o_lantern(1000,1000)

