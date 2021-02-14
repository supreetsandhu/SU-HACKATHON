from random import randint

# Create board
userboard = []

# Populate board
for x in range(5):
    userboard.append(["O"] * 5)

# Format board


def displayb(userboard):
    for row in userboard:
        print(" ".join(row))


# Display board
print("Welcome to the Game of Battleship!")
print("You are able to use one bomb, which will destroy one spot and ")
print("the spot to the right of the choosen spot")
print("Here is your board, o means empty spots and X's will appear on guessed spots!")
print(" ")
displayb(userboard)


def random_row(userboard):
    return randint(1, len(userboard))


def random_col(userboard):
    return randint(1, len(userboard[0]))


sr = random_row(userboard)
sc = random_col(userboard)

# User control
turn = 1
bomb = 1
while turn > 0:
    if bomb == 1:
        choice = input("do you want to use your bomb?(y/n)\n")
        while choice not in ("y", "n"): 
            choice = input("Enter y or n: ") 
        
        if choice == "y":
            print("note try to use a col with 4 or less, so your bomb can be more effective!")
            print(" ")
            bomb=0
            guess_rowBom=int(input("Bomb Row:"))
            guess_colBom=int(input("Bob Col:"))
            for bombOFF in range(2):
                guess_colBom -= 1
                if (guess_rowBom < 1 or guess_rowBom > 6) or (guess_colBom < 1 or guess_colBom > 6):
                    print("not a valid choice.")

                elif(userboard[guess_rowBom-1][guess_colBom-1] == "X"):
                    print("not a valid choice, already picked ")

                else:
                    print("MISS")
                    userboard[guess_rowBom-1][guess_colBom+1]='X'
                    displayb(userboard)


    guess_row=int(input("Guess Row:"))
    guess_col=int(input("Guess Col:"))

    if guess_row == sr and guess_col == sc:
        print("HIT,BATTLESHIP SUNK")
        turn=0

    else:

        if (guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6):
            print("not a valid choice.")

        elif(userboard[guess_row-1][guess_col-1] == "X"):
            print("not a valid choice")

        else:
            print("MISS")
            userboard[guess_row - 1][guess_col - 1]="X"

        if turn == 3:
            print("Game Over.")
    displayb(userboard)
