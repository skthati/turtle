
import random

from turtle import Turtle, Screen

t = Turtle()
ts = Screen()
t.shape("turtle")
t.color("blue")

def forward():
    return t.forward(20)

def right():
    return t.right(90)

def left():
    return t.left(90)

def back():
    return t.back(20)

def func(x):
    return x()


# lst = ["forward", "right", "left", "back"]
# lst = {
#     "forward": forward,
#     "right": right,
#     "left": left,
#     "back": back
# }
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color1 = (r,g,b)
    return random_color1


ts.colormode(255)
lst1 = [forward, right, left, back]
t.pensize(10)

for _ in range(50):
    t.forward(20)
    tup = random_color()
    t.color(tup)
    way = random.choice(lst1)
    func(way)


ts.exitonclick()

