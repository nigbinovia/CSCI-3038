# the random package is imported to be used later in the program 
import random

# this function gets the next move from the user and checks if
# said move is valid 
def GetMove():
  
# assuming the user input will be true, the user is prompted to enter
# their x and y coordinates of choice 
    while True:
        x = input("Enter your x coordinate: ")
        y = input("Enter your y coordinate: ")

# if the user enters a number for both coordinates, the program validates
#the values and moves on to the next check 
        if (x.isdigit() and y.isdigit()):
            x = int(x)
            y = int(y)

# if the given x and y coordinates are within bounds, the program breaks
# out of the if statement loop and returns the x and y values to the 
# function call
            if (0 <= x < 9 and 0 <= y < 9):
                break

# if either coordinate is out of bounds, an error message is prompted to the 
# user of this issue and asks the user to reenter a better option
            else:
                print("These coordinates are invalid. Please try again.")

# if either if of the coordinates aren't a number, an error message is prompted
# to the user of this issue and asks the user to reenter a better option 
        else:
            print("Invalid input. Please enter integers for x and y.")

    return x, y

  

# this function prints current game grid to the user 
def PrintGrid(userGrid):

# this code segment prints the x-axis above the grid
    print(" ", end="")
    for i in range(9):
        print(i, end=" ")
    print("\n")

# this code segment prints the y-axis and the current layout of the 
# game to the user 

    for i in range(9):
        print(i, end=" ")
        for j in range(9):
            print(userGrid[i][j], end=" ")
        print()

# this is a recursively called function that is used to find all bordering mines 
# for each user move 
def BorderMines(row, col, mines, gridCheck):

# this count variable tracks how many mines border a coordinate 
    count = 0

# if the spot above the coordinate is found within bounds and is next to mine, 
# the count increases
    if (0 <= row - 1 < 9) and (gridCheck[row-1][col] == '*'):
        count = count + 1

# if the spot below the coordinate is found within bounds and is next to mine, 
# the count increases
    if (0 <= row + 1 < 9) and (gridCheck[row+1][col] == '*'):
        count = count + 1

# if the spot to the left of the coordinate is found within bounds and is next to mine, 
# the count increases
    if (0 <= col - 1 < 9) and (gridCheck[row][col-1] == '*'):
        count = count + 1

# if the spot to the right of the coordinate is found within bounds and is next to mine, 
# the count increases
    if (0 <= col + 1 < 9) and (gridCheck[row][col+1] == '*'):
        count = count + 1

# if the spot to the upper left of the coordinate is found within bounds and is next to mine, 
# the count increases
    if (0 <= row - 1 < 9) and (0 <= col - 1 < 9) and (gridCheck[row-1][col-1] == '*'):
        count = count + 1

# if the spot to the upper right of the coordinate is found within bounds and is next to mine, 
# the count increases
    if (0 <= row - 1 < 9) and (0 <= col + 1 < 9) and (gridCheck[row-1][col+1] == '*'):
        count = count + 1

# if the spot to the bottom left of  the coordinate is found within bounds and is next to mine, 
# the count increases
    if (0 <= row + 1 < 9) and (0 <= col - 1 < 9) and (gridCheck[row+1][col-1] == '*'):
        count = count + 1

# if the spot to the bottom right of the coordinate is found within bounds and is next to mine, 
# the count increases
    if (0 <= row + 1 < 9) and (0 <= col + 1 < 9) and (gridCheck[row+1][col+1] == '*'):
        count = count + 1

# the count of the given coordinate is returned to the function call
    return count

# after the game starts, this function is called until the user wins or loses
def LoopGame(userGrid, gridCheck, mines, row, col, lastMoves):

# if the user enters a move that has already been revealed, false is returned 
    if (userGrid[row][col] != '-'):
        return False

# if the user enters a move that is a confirmed mine on both grids, all mines 
# are displayed to the user and the game ends 
    if (gridCheck[row][col] == '*'):
        userGrid[row][col] = '*'

        for i in range(len(mines)):
            userGrid[mines[i][0]][mines[i][1]] = '*'

# a losing message is prompted to the user true is returned to end the loop at the 
# function call 
        print("\n")
        PrintGrid(userGrid)
        print("\n")
        print("You lost!")
        return True

# if the user suceeds past these if statements, the given coordinates count is assigned and 
# a remaining move is subtracted from the user 
    else:
        count = BorderMines(row, col, mines, gridCheck)
        lastMoves = lastMoves - 1
      
# the count is displayed on the grid as well
        userGrid[row][col] = str(count)

# if no neighboring mines have been checked for yet with the given coordinate, the prior 
# recursive checks used again to find possible neighboring mines 
        if count == 0:

# if the spot above the coordinate is found within bounds and isn't next to mine, 
# the LoopGame function is called again to expand the coordinate's range 
            if (0 <= row - 1 < 9) and (gridCheck[row-1][col] != '*'):
              LoopGame(userGrid, gridCheck, mines, row - 1, col, lastMoves)
              
# if the spot below the coordinate is found within bounds and isn't next to mine, 
# the LoopGame function is called again to expand the coordinate's range 
            if (0 <= row + 1 < 9) and (gridCheck[row+1][col] != '*'):
                LoopGame(userGrid, gridCheck, mines, row + 1, col, lastMoves)
              
# if the spot to the left of the coordinate is found within bounds and isn't next to mine, 
# the LoopGame function is called again to expand the coordinate's range 
            if (0 <= col - 1 < 9) and (gridCheck[row][col-1] != '*'):
                LoopGame(userGrid, gridCheck, mines, row, col - 1, lastMoves)

# if the spot to the right of the coordinate is found within bounds and isn't next to mine, 
# the LoopGame function is called again to expand the coordinate's range 
            if (0 <= col + 1 < 9) and (gridCheck[row][col+1] != '*'):
                LoopGame(userGrid, gridCheck, mines, row, col + 1, lastMoves)

# if the spot to the upper left of the coordinate is found within bounds and isn't next to mine, 
# the LoopGame function is called again to expand the coordinate's range 
            if (0 <= row - 1 < 9) and (0 <= col - 1 < 9) and (gridCheck[row-1][col-1] != '*'):
                LoopGame(userGrid, gridCheck, mines, row - 1, col - 1, lastMoves)

# if the spot to the uppe right of the coordinate is found within bounds and isn't next to mine, 
# the LoopGame function is called again to expand the coordinate's range             
            if (0 <= row - 1 < 9) and (0 <= col + 1 < 9) and (gridCheck[row-1][col+1] != '*'):
                LoopGame(userGrid, gridCheck, mines, row - 1, col + 1, lastMoves)

# if the spot to the bottom left of the coordinate is found within bounds and isn't next to mine, 
# the LoopGame function is called again to expand the coordinate's range 
            if (0 <= row + 1 < 9) and (0 <= col - 1 < 9) and (gridCheck[row+1][col-1] != '*'):
                LoopGame(userGrid, gridCheck, mines, row + 1, col - 1, lastMoves)

# if the spot to the bottom right of the coordinate is found within bounds and isn't next to mine, 
# the LoopGame function is called again to expand the coordinate's range 
            if (0 <= row + 1 < 9) and (0 <= col + 1 < 9) and (gridCheck[row+1][col+1] != '*'):
                LoopGame(userGrid, gridCheck, mines, row + 1, col + 1, lastMoves)

# false is returned so the game continues 
        return False


#this function initalizes sets up the game 
def StartGame():

# the variables are defined 
    over = False
    gridCheck = [['-'] * 9 for _ in range(9)]
    userGrid = [['-'] * 9 for _ in range(9)]
    lastMoves = 9 * 9 - 10
    userMoves = 0
    mines = []

# the random number generator is initialized 
    random.seed()

# both grids are get up with "-" as placeholders
    for i in range(9):
        for j in range(9):
            userGrid[i][j] = gridCheck[i][j] = '-'
  
# a boolean 2D array called taken is defined and used to place 
# the mines for the game 
    taken = [False] * (9 * 9)

# while the mine limit hasn't been reaches
    while (len(mines) < 10):
# a random number between 0 and 80 is found and used to create the x and y 
# coordinate for a mine 
        position = random.randint(0, 9 * 9 - 1)
        x = position // 9
        y = position % 9

# if the newly created mine isn't a repeat on the grid, the mine is 
# tracked in the mines array, placed on the checking grid, and marked 
# off on the taken array 
        if (taken[position] == False):
            mines.append([x, y])
            gridCheck[x][y] = '*'
            taken[position] = True

    
# while the game isn't over 
    while (over == False):
# the current status of the game is printed 
        print("\n")
        print("Current Status of Grid: ")
        PrintGrid(userGrid)

# the user is prompted to enter their move
        x, y = GetMove()

# if this is the user's first move, the rules go that
# if the user hits a mine on their first try, the mine is 
# replaced 
        if userMoves == 0:
             if gridCheck[x][y] == '*': 
                for i in range(9):
                  for j in range(9):
                    if gridCheck[i][j] != '*':
                      gridCheck[i][j] = '*'
                      gridCheck[x][y] = '-'
                      return
                
# the program moves on to the user's next move 
        userMoves  = userMoves + 1

# this code line checks if the LoopGame has returned true or not 
        over = LoopGame(userGrid, gridCheck, mines, x, y, lastMoves)

# the game isn't declared over in the LoopGame function and the user is 
# out of moves, the user is prompted as the winner 
        if (over == False) and (lastMoves == 0):
            print("\n")
            print("You won!")
# over is set to true so the program loop ends 
            over = True

# this function call calls the game to start
StartGame()
