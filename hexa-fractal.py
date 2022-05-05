import turtle
import random

tw = turtle.Screen()
tw.screensize(2000, 2000)
tw.bgcolor("black")

turtle.penup()
turtle.back(200)
turtle.right(90)
turtle.forward(350)
turtle.left(90)
turtle.pendown()
turtle.color("white")
turtle.speed("fastest")

bottom = {}
bot_right = {}
top_right = {}
top = {}
top_left = {}
bot_left = {}

def draw_hexagon():
    bottom[turtle.xcor()] = turtle.ycor()
    turtle.forward(400)
    turtle.left(60)
    bottom[turtle.xcor()] = turtle.ycor()

    bot_right[turtle.xcor()] = turtle.ycor()
    turtle.forward(400)
    turtle.left(60)
    bot_right[turtle.xcor()] = turtle.ycor()

    top_right[turtle.xcor()] = turtle.ycor()
    turtle.forward(400)
    turtle.left(60)
    top_right[turtle.xcor()] = turtle.ycor()

    top[turtle.xcor()] = turtle.ycor()
    turtle.forward(400)
    turtle.left(60)
    top[turtle.xcor()] = turtle.ycor()

    top_left[turtle.xcor()] = turtle.ycor()
    turtle.forward(400)
    turtle.left(60)
    top_left[turtle.xcor()] = turtle.ycor()

    bot_left[turtle.xcor()] = turtle.ycor()
    turtle.forward(400)
    turtle.left(60)
    bot_left[turtle.xcor()] = turtle.ycor()

    turtle.penup()


def draw_fractal():
    x3 = 125
    y3 = 18

    for i in range(100000):
        point_dict = random.choice([bottom, bot_right, top_right, top, top_left, bot_left])

        x1, y1 = list(point_dict.items())[0]
        x2, y2 = list(point_dict.items())[1]

        centroid_point = ((x1+x2+x3)/3, (y1+y2+y3)/3)

        x3 = centroid_point[0]
        y3 = centroid_point[1]

        turtle.penup()
        turtle.goto(centroid_point)
        turtle.pendown()
        turtle.color("white")
        turtle.dot(1)
        turtle.penup()

draw_hexagon()
draw_fractal()