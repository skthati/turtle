import random

from turtle import Turtle, Screen

t = Turtle()
w = Turtle()

w.penup()
w.goto(0, 200)
w.pendown()
w.color("blue")
w.pensize(2)
w.hideturtle()
w.write("Hello", align="center", font=("Arial", 24, "normal"))


ts = Screen()
ts.colormode(255)
ts.setup(700, 700)

''' t turtle'''
t.shape("turtle")
t.color("blue")
t.pensize(5)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color1 = (r,g,b)
    return random_color1


def move_forward():
    tup = random_color()
    t.color(tup)
    t.forward(20)
    w.clear()
    w.write("Forward 20", align="center", font=("Arial", 24, "normal"))



def right_move():
    tup = random_color()
    t.color(tup)
    t.right(90)
    w.clear()
    w.write("Right 90", align="center", font=("Arial", 24, "normal"))


def left_move():
    tup = random_color()
    t.color(tup)
    t.left(90)
    w.clear()
    w.write("Left 90", align="center", font=("Arial", 24, "normal"))


def move_backward():
    tup = random_color()
    t.color(tup)
    t.backward(20)
    w.clear()
    w.write("Backward 20", align="center", font=("Arial", 24, "normal"))


def go_home():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

ts.listen()
ts.onkey(key="Up", fun=move_forward)
ts.onkey(key="Right", fun=right_move)
ts.onkey(key="Left", fun=left_move)
ts.onkey(key="Down", fun=move_backward)
ts.onkey(key="space", fun=go_home)


ts.exitonclick()




