import turtle


def gotoRow(x, y):
    t.penup()
    t.goto(-140, -140)
    t.setx(-140 + abs(70 * (x-1)))
    t.sety(-140+ abs(70 * (y - 1)))
    stamp("red")


def stamp(color):
    t.pendown()
    t.shape("square")
    t.shapesize(3.35)
    t.color(color)
    t.stamp()
    t.penup()

# 0--------------------------------


def square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

# 5,70,i


def row(n, size, i):
    for j in range(n):
        square(size)
        t.forward(size)

    t.penup()
    t.forward(40)
    style = ('Courier', 50, 'italic')
    t.write(i+1, font=style, align='center')
    t.forward(-40)

    t.penup()
    t.left(180)
    t.forward(n * size)
    t.left(180)
    t.pendown()

# 3,5,70


def row_of_rows(m, n, size):
    for i in range(m):
        row(n, size, i)
        t.penup()
        t.left(90)
        t.forward(size)
        t.right(90)
        t.pendown()
    t.penup()
    t.right(90)
    t.forward(m * size)
    t.left(90)
    t.pendown()


def printpos(x, y):
    print(x, y)


t = turtle.Turtle()
t.hideturtle()
t.speed(2000)
wn = turtle.Screen()
wn.bgcolor("black")
# wn.onclick(printpos)
t.color("white")
t.penup()
t.goto(0, 250)
t.pendown()

style = ('Courier', 50, 'italic')
t.write('Battleship', font=style, align='center')

t.penup()
t.goto(-140, -260)
t.pendown()

for i in range(5):
    style = ('Courier', 50, 'italic')
    t.write(i+1, font=style, align='center')
    t.penup()
    t.forward(70)

t.penup()
t.goto(-175, -175)
t.pendown()

x = 5
y = 5
size = 70
row_of_rows(x, y, size)

gotoRow(3, 2)
gotoRow(3, 3)
gotoRow(2, 1)
gotoRow(2, 2)
gotoRow(4, 1)
gotoRow(1, 5)


turtle.exitonclick()
