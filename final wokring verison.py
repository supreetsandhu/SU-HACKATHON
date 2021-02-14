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
print("Here is your board, o means empty spots!")
displayb(userboard)

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
        print ("HIT, ONE BATTLESHIP SUNK")
        break
    
    else:
        
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print ("not a valid choice.")
        
        elif(userboard[guess_row-1][guess_col-1] == "X"):
            print ("not a valid choice")
        
        else:
            print ("MISS")
            userboard[guess_row - 1][guess_col - 1] = "X"
        
        if turn == 3:
            print ("Game Over.")
    
    print ("Turn" + str((turn + 1)))
    displayb(userboard)