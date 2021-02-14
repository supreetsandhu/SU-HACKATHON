import turtle


def gotoRow(x, y, color):
    t.penup()
    t.goto(-140, -140)
    t.setx(-140 + abs(70 * (x-1)))
    t.sety(-140 + abs(70 * (y - 1)))
    stamp(color)


def stamp(color):
    t.pendown()
    t.shape("square")
    t.color(color)
    t.stamp()


def square(side):
    for i in range(4):
        t.forward(side)
        t.left(90)


def row(n, side, i):
    t.penup()
    t.forward(-40)
    style = ('Courier', 50, 'italic')
    t.write(i+1, font=style, align='center')
    t.forward(40)
    t.pendown()

    for j in range(n):
        square(side)
        t.forward(side)

    t.penup()
    t.left(180)
    t.forward(n * side)
    t.left(180)
    t.pendown()


def row_of_rows(m, n, side):
    for i in range(m):
        row(n, side, i)
        t.penup()
        t.left(90)
        t.forward(side)
        t.right(90)
        t.pendown()
    t.penup()
    t.right(90)
    t.forward(m * side)
    t.left(90)
    t.pendown()


t = turtle.Turtle()
t.hideturtle()
t.speed(200)
wn = turtle.Screen()
wn.bgcolor("black")
t.color("white")
t.penup()

t.setpos(0, 250)
style = ('Courier', 50, 'italic')
t.write('Battleship', font=style, align='center')

t.setpos(0, 180)
style2 = ('Courier', 20)
t.write('Computer', font=style2, align='center')

t.setpos(260, 180)
t.shapesize(1.35)
t.write('miss', font=style2, align='center')
t.setpos(260, 160)
stamp("blue")
t.penup()

t.setpos(340, 180)
t.color("white")
t.write('hit', font=style2, align='center')
t.setpos(340, 160)
stamp("red")
t.penup()


t.penup()
t.setpos(-140, -260)
t.shapesize(3.35)
t.pendown()
t.color("white")

for i in range(5):
    style = ('Courier', 50, 'italic')
    t.write(i + 1, font=style, align='center')
    t.penup()
    t.forward(70)

t.penup()
t.setpos(-175, -175)
t.pendown()

row_of_rows(5, 5, 70)
gotoRow(3, 2, "red")

turtle.mainloop()
