
# import package and making objects

import turtle


def square(side):
    for i in range(4):
        t.forward(side)
        t.left(90)


def row(n, side):
    for i in range(n):
        square(side)
        t.forward(side)

    
    style = ('Courier', 50, 'italic')
    t.write('1', font=style, align='center')

    t.penup()
    t.left(180)
    t.forward(n * side)
    t.left(180)
    t.pendown()


def row_of_rows(m, n, side):
    for i in range(m):
        row(n, side)
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
t.pendown()

style = ('Courier', 50, 'italic')
t.write('Battleship', font=style, align='center'

t.penup()
t.setpos(-175, -175)
t.pendown()

row_of_rows(5, 5, 70)

turtle.mainloop()
