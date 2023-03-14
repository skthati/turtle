import random

from turtle import Turtle, Screen


ts = Screen()
ts.colormode(255)
ts.setup(600,600)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color1 = (r,g,b)
    return random_color1


def random_speed():
    return random.randint(1, 10)


y = "A"
j = 50
x = -280

t = Turtle()
t.penup()
t.shape("turtle")
t.color(random_color())
t.goto(-280, (-200+j))
j += 50

while x < 250:
    x, l = t.position()
    t.forward(random_speed())



ts.exitonclick()






