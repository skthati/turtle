import random

from turtle import Turtle, Screen

t = Turtle()
ts = Screen()
t.shape("turtle")
t.color("blue")


# Draw a square
t.penup()
t.goto(-300,-200)
t.pendown()
for i in range(4):
    t.forward(100)
    t.right(90)

# Draw a dashed line
t.penup()
t.goto(-150,-200)
t.pendown()
for _ in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

 # Draw triangle, square, upto 10 sides with each random color

# c = ["red", "yellow", "blue", "green", "black", "pink", "orange", "gray", "purple"]
# c = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white"]
# c = ["turquoise"]
# sides = 3
# while sides < 10:
#     for _ in range(sides):
#         shape = 360 / sides
#         t.forward(100)
#         t.right(shape)
#     t.color(random.choice(c))
#     sides += 1

# way = ["forward(50)", "backward(50)", "left(50)", "back(50)"]
# way = [t.forward(10), t.backward(10), t.left(10), t.right(10)]
# y = [0, 1, 2, 3]
# t_drection = [0, 90, 180, 270]
# direction = {
#     1: "forward",
#     2: "backward",
#     3: "left",
#     4: "right"
# }
# for _ in range(100):
#     t.forward(10)
#     # t_direction_temp = random.choice(t_drection)
#     # t.right(random.choice(t_drection))
#     x = random.randint(1,4)
#     if x == 1:
#         t.forward(10)
#     elif x == 2:
#         t.backward(10)
#     elif x == 3:
#         t.left(90)
#     elif x == 4:
#         t.right(90)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color1 = (r,g,b)
    return random_color1


ts.colormode(255)
# direction = [0, 90, 180, 270]
#
t.pensize(3)
t.speed(100)
sides = 3
t.penup()
t.goto(-50,300)
t.pendown()
while sides < 30:

    for _ in range(sides):
        shape = 360 / sides
        t.forward(50)
        t.right(shape)
        tup = random_color()
        t.color(tup)
    sides += 1
# for _ in range(500):
#     # t.setheading(random.choice(direction))
#     tup = random_color()
#     t.color(tup)
#     # t.color("blue")
#     # t.color(random.choice(c))
#     t.circle(150)
#     t.right(1)










ts.exitonclick()

