from random import randint
import turtle
import time

# graphics ----------------------------


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


def square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)


def row(n, size, i):
    t.penup()
    t.forward(-40)
    style = ('Courier', 50, 'italic')
    t.write(i+1, font=style, align='center')
    t.forward(40)
    t.pendown()

    for j in range(n):
        square(size)
        t.forward(size)

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


# Create board
userboard = []
t = turtle.Turtle()

# Populate board
for x in range(5):
    userboard.append(["O"] * 5)

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

def checkspot(r, c):
    if(r-1 == sr and c-1 == sc):
        return 0
    if(r-1 == sr2 and c-1 == sc2):
        return 0
    return 1


print("Welcome to the Game of Battleship!")
print("You are able to use one bomb, which will destroy one spot and ")
print("the spot to the right of the chosen spot")
print("Here is your board - please navigate to the popup window")
print("Your goal is to find the two spots that has the ship.")
print(" ")


def random_row(userboard):
    return (randint(0, 4))


def random_col(userboard):
    return (randint(0, 4))


sr = random_row(userboard)
sc = random_col(userboard)
sr2 = random_row(userboard)
while(sr == sr2):
    sr2 = random_row(userboard)
sc2 = random_col(userboard)
while(sc == sc2):
    sc2 = random_col(userboard)

# User control
turn = 1
bomb = 1
shipleft = 2
while shipleft > 0:
    if bomb == 1:
        choice = turtle.textinput("", "do you want to use your bomb?(y/n)")
        while choice not in ("y", "n"):
            choice = name = turtle.textinput("", "Enter y or n:")

        if choice == "y":
            print(
                "note try to use a col with 4 or less, so your bomb can be more effective!")
            print(" ")
            bomb = 0
            guess_rowBom = int(turtle.numinput(" ", "Enter Bomb Col"))
            guess_colBom = int(turtle.numinput(" ", "Enter Bomb Row"))
            for bombOFF in range(2):
                if (guess_rowBom < -1 or guess_rowBom > 5) or (guess_colBom < -1 or guess_colBom > 5):
                    print("not a valid choice.")

                elif(userboard[guess_rowBom-1][guess_colBom-1] == "X"):
                    print("not a valid choice, already picked ")
                elif(checkspot(guess_rowBom, guess_colBom) == 0):
                    shipleft -= 1
                    print("HIT,BATTLESHIP SUNK")
                    userboard[guess_rowBom - 1][guess_colBom - 1] = "S"
                    gotoRow(guess_rowBom, guess_colBom, "red")
                    stamp("red")
                    if (shipleft == 0):
                        turn = 0
                        break
                else:
                    userboard[guess_rowBom - 1][guess_colBom - 1] = 'X'
                    gotoRow(guess_rowBom, guess_colBom, "blue")
                guess_rowBom += 1

    if shipleft != 0:
        guess_row = int(turtle.numinput("", "Enter Col"))
        guess_col = int(turtle.numinput("", "Enter Row"))

        if (checkspot(guess_row, guess_col) == 0):
            shipleft -= 1
            print("HIT,BATTLESHIP SUNK")
            userboard[guess_row - 1][guess_col - 1] = "S"
            gotoRow(guess_row, guess_col, "red")
            stamp("red")
            if(shipleft == 0):
                turn = 0

        else:

            if (guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6):
                print("not a valid choice.")

            elif(userboard[guess_row-1][guess_col-1] == "X"):
                print("not a valid choice")

            else:
                userboard[guess_row - 1][guess_col - 1] = "X"
                gotoRow(guess_row, guess_col, "blue")
if shipleft == 0:
    time.sleep(2)
    print("Game Over!")
