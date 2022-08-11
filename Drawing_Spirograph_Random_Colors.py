import turtle
import random

Nu_Pagadzi = turtle.Turtle()
turtle.colormode(255)
Nu_Pagadzi.hideturtle();

def random_color_picker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


Nu_Pagadzi.speed(0)
current_heading = Nu_Pagadzi.heading()


def draw_spiragraph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        Nu_Pagadzi.pencolor(random_color_picker())
        Nu_Pagadzi.circle(100)
        Nu_Pagadzi.setheading(Nu_Pagadzi.heading() + size_of_gap)


draw_spiragraph(4)
screen = turtle.Screen()
screen.exitonclick()