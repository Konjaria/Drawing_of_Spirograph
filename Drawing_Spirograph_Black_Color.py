import turtle
import random

Nu_Pagadzi = turtle.Turtle()

Nu_Pagadzi.speed(0)
current_heading = Nu_Pagadzi.heading()
Nu_Pagadzi.hideturtle();


def draw_spiragraph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        Nu_Pagadzi.pencolor("black")
        Nu_Pagadzi.circle(100)
        Nu_Pagadzi.setheading(Nu_Pagadzi.heading() + size_of_gap)


draw_spiragraph(4)
screen = turtle.Screen()
screen.exitonclick()