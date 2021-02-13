import random
random.seed(0)

rows, cols = (5, 5) 
userGuesses=[] 
compBoard = []


for i in range(cols): 
    col = [] 
    for j in range(rows): 
        col.append('-') 
    userGuesses.append(col) 
    compBoard.append(col) 


count = 0
for x in range(3): 
 temprow = random.randint(0, 4)
 tempcol = random.randint(0, 4)
 compBoard[temprow][tempcol] = 's'
 compBoard[temprow][tempcol+1] ='s'
    
   



print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in compBoard]))