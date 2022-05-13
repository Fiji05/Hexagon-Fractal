import turtle
import random
import cairosvg
import os
import tempfile
import canvasvg
import shutil

bottom = {}
bot_right = {}
top_right = {}
top = {}
top_left = {}
bot_left = {}

def draw_hexagon():
    turtle.pendown()

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


def draw_fractal(amt):
    x3, y3 = random.randint(1, 200), random.randint(1, 200)

    for i in range(amt):
        point_dict = random.choice([bottom, bot_right, top_right, top, top_left, bot_left])

        x1, y1 = list(point_dict.items())[0]
        x2, y2 = list(point_dict.items())[1]

        centroid_point = ((x1+x2+x3)/3, (y1+y2+y3)/3)

        x3 = centroid_point[0]
        y3 = centroid_point[1]

        turtle.goto(centroid_point)
        turtle.pendown()
        turtle.stamp()
        turtle.penup()

while True:
    amt = int(input("Enter amount of points to create: "))   

    if amt:
        tw = turtle.Screen()
        tw.screensize(2000, 2000)
        tw.bgcolor("black")

        turtle.penup()
        turtle.back(200)
        turtle.right(90)
        turtle.forward(350)
        turtle.left(90)
        turtle.color("white")
        turtle.speed("fastest")
        turtle.shape("circle")
        turtle.shapesize(0.01)

        draw_hexagon()
        draw_fractal(amt)

        nameSav = f"fractal_{amt}_points.png"
        tmpdir = tempfile.mkdtemp()
        tmpfile = os.path.join(tmpdir, 'tmp.svg')
        ts = turtle.getscreen().getcanvas()
        canvasvg.saveall(tmpfile, ts)
        with open(tmpfile) as svg_input, open(nameSav, 'wb') as png_output:
            cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)
        shutil.rmtree(tmpdir)  # clean up temp file(s)


        break
    
    else:
        continue