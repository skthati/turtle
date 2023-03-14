import random

from turtle import Turtle, Screen

t = Turtle()
s = Turtle()
a = Turtle()
n = Turtle()
d = Turtle()

ts = Screen()
ts.colormode(255)
ts.setup(700, 700)

''' t turtle'''
t.shape("turtle")
t.color("blue")
t.pensize(5)

''' s turtle'''
s.shape("turtle")
s.color("red")
s.pensize(5)

''' a turtle'''
a.shape("turtle")
a.color("red")
a.pensize(5)

''' n turtle'''
n.shape("turtle")
n.color("red")
n.pensize(5)

''' d turtle'''
d.shape("turtle")
d.color("red")
d.pensize(5)


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


def right_move():
    tup = random_color()
    t.color(tup)
    t.right(90)


def left_move():
    tup = random_color()
    t.color(tup)
    t.left(90)


def move_backward():
    tup = random_color()
    t.color(tup)
    t.backward(20)


def go_home():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


t.goto(-300, -300)

ts.listen()
ts.onkey(key="Up", fun=move_forward)
ts.onkey(key="Right", fun=right_move)
ts.onkey(key="Left", fun=left_move)
ts.onkey(key="Down", fun=move_backward)
ts.onkey(key="space", fun=go_home)


ts.exitonclick()




