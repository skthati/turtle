import random
from turtle import Turtle, Screen

players = {}

players_lst = []
new_players_lst = []
ts = Screen()
ts.colormode(255)
ts.bgpic("giphy.gif")

ln = Turtle()
ln.penup()
ln.goto(250, -150)
ln.pensize(10)
ln.pendown()
ln.left(90)
ln.forward(350)
ln.penup()
ln.isvisible()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color1 = (r,g,b)
    return random_color1


def random_speed():
    return random.randint(1, 10)


for i in range(1, 5):
    players_lst.append("A"+str(i))

# for i in range(4):
#     globals()[players_lst[i]] = players_lst[i]
#     # print(type(players_lst[i]))

print(players_lst)
print(type(players_lst))

j = 50

for i in range(4):
    players_lst[i] = Turtle()
    t = players_lst[i]
    t.penup()
    t.color(random_color())
    t.shape("turtle")
    t.goto(-250, (-100+j))
    j += 50

x = -250

while x < 230:
    for i in range(4):
        x, x1 = players_lst[i].position()
        players_lst[i].forward(random_speed())
        a, b = players_lst[i].position()
        if a >= 230:

            print(f"{players_lst[i]} Won the race!")
            break




# players_lst[0].color("blue")
# players_lst[0].goto(0, -100)
#
# players_lst[1].color("red")
# players_lst[1].goto(0, -200)


ts.exitonclick()

# for i in range(5):
#     players["A" + str(i)] = "A" + str(i)
#
# for i in players:
#     print(f"{i} : {players[i]}")
#     vars()[i] = players[i]
#     players_lst.append(globals()[players[i]])
#
# print(players_lst)
# print(type(players_lst))


