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

# # Format board
# def displayb(userboard):
#     for row in userboard:
#         print(" ".join(row))


# Display board
print("Welcome to the Game of Battleship!")
print("You are able to use one bomb, which will destroy one spot and ")
print("the spot to the right of the chosen spot")
print("Here is your board, o means empty spots and X's will appear on guessed spots!")
print(" ")
# displayb(userboard)


def random_row(userboard):
    row = randint(1, len(userboard))
    print(row)
    return row


def random_col(userboard):
    col = randint(1, len(userboard[0]))
    print(col)
    return col


sr = random_row(userboard)
sc = random_col(userboard)

# User control
turn = 1
bomb = 1
while turn > 0:
    if bomb == 1:
        choice = turtle.textinput("do you want to use your bomb?(y/n)", "bomb?")
        # choice = input("do you want to use your bomb?(y/n)\n")
        while choice not in ("y", "n"):
            choice = name = turtle.textinput("Enter y or n:", "bomb?")
            # choice = input("Enter y or n: ")

        if choice == "y":
            print(
                "note try to use a col with 4 or less, so your bomb can be more effective!")
            print(" ")
            bomb = 0
            # guess_rowBom = int(input("Bomb Row:"))
            # guess_colBom = int(input("Bob Col:"))
            guess_rowBom = int(turtle.numinput("Enter Bomb Row", "row"))
            guess_colBom = int(turtle.numinput("Enter Bomb Col", "col"))
            for bombOFF in range(2):
                guess_colBom -= 1
                if (guess_rowBom < 1 or guess_rowBom > 6) or (guess_colBom < 1 or guess_colBom > 6):
                    print("not a valid choice.")

                elif(userboard[guess_rowBom-1][guess_colBom-1] == "X"):
                    print("not a valid choice, already picked ")

                else:
                    print("MISS")
                    userboard[guess_rowBom-1][guess_colBom+1] = 'X'
                    # displayb(userboard)
                    gotoRow(guess_rowBom, guess_colBom, "blue")

    guess_row = int(turtle.numinput("Enter Row", "row"))
    guess_col = int(turtle.numinput("Enter Col", "col"))
    # guess_row = int(input("Guess Row:"))
    # guess_col = int(input("Guess Col:"))

    if guess_row == sr and guess_col == sc:
        print("HIT,BATTLESHIP SUNK, ending game..")
        gotoRow(guess_row, guess_col, "red")
        stamp("red")
        time.sleep(2)
        turn = 0

    else:

        if (guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6):
            print("not a valid choice.")

        elif(userboard[guess_row-1][guess_col-1] == "X"):
            print("not a valid choice")

        else:
            print("MISS")
            userboard[guess_row - 1][guess_col - 1] = "X"
            gotoRow(guess_row, guess_col, "blue")

        if turn == 3:
            print("Game Over.")
    # displayb(userboard)
