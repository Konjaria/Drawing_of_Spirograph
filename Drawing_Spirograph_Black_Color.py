import turtle
import random

painter = turtle.Turtle()

painter.speed(0)
current_heading = painter.heading()
painter.hideturtle();


def draw_spiragraph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        painter.pencolor("black")
        painter.circle(100)
        painter.setheading(painter.heading() + size_of_gap)


draw_spiragraph(4)
screen = turtle.Screen()
screen.exitonclick()
