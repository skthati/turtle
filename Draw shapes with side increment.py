import random
from turtle import Turtle, Screen

t = Turtle()
ts = Screen()
t.shape("turtle")

#  Draw triangle, square, upto 10 sides with each random color

c = ["red", "yellow", "blue", "green", "black", "pink", "orange", "gray", "purple"]

sides = 3
while sides < 10:
    for _ in range(sides):
        shape = 360 / sides
        t.forward(100)
        t.right(shape)
    t.color(random.choice(c))
    sides += 1

ts.exitonclick()