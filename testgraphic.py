from random import randint
import turtle
import time

# graphics ----------------------------


def gotoRow(x, y, color):
    t.penup()
    t.goto(-140, -140)
    t.setx(-140 + abs(70 * (x-1)))
    t.sety(-140+ abs(70 * (y - 1)))
    stamp(color)


def stamp(color):
    t.pendown()
    t.shape("square")
    t.shapesize(3.35)
    t.color(color)
    t.stamp()

def square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)


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


print("welcome to battleship!")
# Create board
userboard = []
t = turtle.Turtle()

# Populate board
for x in range(5):
    userboard.append(["O"] * 5)


t.hideturtle()
t.speed(500)
wn = turtle.Screen()
wn.bgcolor("black")
t.color("white")
t.penup()
t.setpos(0, 250)
t.pendown()

style = ('Courier', 50, 'italic')
t.write('Battleship', font=style, align='center')

t.penup()
t.setpos(-140, -260)
t.pendown()

for i in range(5):
    style = ('Courier', 50, 'italic')
    t.write(i+1, font=style, align='center')
    t.penup()
    t.forward(70)

t.penup()
t.setpos(-175, -175)
t.pendown()

row_of_rows(5, 5, 70)

# Format board
# def displayb(userboard):
#     for row in userboard:
#         print(" ".join(row))

# Display board
print("Here is your board, o means empty spots!")
# displayb(userboard)

def random_row(userboard):
    return randint(1, len(userboard))


def random_col(userboard):
    return randint(1, len(userboard[0]))


sr = random_row(userboard)
sc = random_col(userboard)

# User control
for turn in range(4):

    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == sr and guess_col == sc:
        print("HIT, ONE BATTLESHIP SUNK")
        gotoRow(guess_row, guess_col, "red")

    else:

        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print("not a valid choice.")

        elif(userboard[guess_row-1][guess_col-1] == "X"):
            print("not a valid choice")

        else:
            print("MISS")
            #userboard[guess_row - 1][guess_col - 1] = "X"
            gotoRow(guess_row, guess_col, "blue")

        if turn == 3:
            print("Game Over.")

    print("Turn" + str((turn + 1)))
    #displayb(userboard)


