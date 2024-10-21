import random
import colorgram
from turtle import Turtle, Screen, colormode

colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("MidnightBlue")
timmy_the_turtle.speed('fastest')
timmy_the_turtle.fillcolor()

directions = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    line_color = (r, g, b)
    return line_color


def random_path():
    timmy_the_turtle.pensize(10)
    for _ in range(200):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.forward(20)
        timmy_the_turtle.setheading(random.choice(directions))

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

def damien_hirst(image):
    colors = colorgram.extract(image, 30)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if r + g + b <= 720:
            new_color = (r, g, b)
            rgb_colors.append(new_color)

    start_y = -380
    timmy_the_turtle.penup()



    while start_y < 381:
        timmy_the_turtle.goto(-400, start_y)

        for _ in range(20):
            timmy_the_turtle.color(random.choice(rgb_colors))
            timmy_the_turtle.pendown()

            timmy_the_turtle.fillcolor()
            timmy_the_turtle.begin_fill()
            timmy_the_turtle.circle(10)
            timmy_the_turtle.end_fill()
            timmy_the_turtle.penup()
            timmy_the_turtle.forward(40)

        timmy_the_turtle.pendown()
        timmy_the_turtle.fillcolor()
        timmy_the_turtle.begin_fill()
        timmy_the_turtle.circle(10)
        timmy_the_turtle.end_fill()
        timmy_the_turtle.penup()
        start_y += 40



damien_hirst('image.jpeg')


















screen = Screen()
screen.exitonclick()
