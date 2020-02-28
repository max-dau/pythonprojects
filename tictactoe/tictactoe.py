from time import sleep

#get player input as a coordinate and check whether it will work with the program
viableCoords = ['1', '2', '3']

def getInput(player):
    while True:
        coords = input('Where do you want to place your symbol?\n')
        if coords[0] not in viableCoords or coords[1] not in viableCoords:
            print('Your input seems to be illogical. Please try again.')
            continue
        elif grid[int(coords[0])-1][int(coords[1])-1] != ' ':
            print('There already is a symbol in this spot. please choose another one.')
        else:
            grid[int(coords[0])-1][int(coords[1])-1] = player
            break


#All lines get filled with "-" for empty at the beginning
grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

#Checks the board for a win, takes every symbol and tests for a line going horizontal, vertical, or across
def checkForWin():
    row = 0
    while row < 3:
        if grid[row][0] == grid[row][1] == grid[row][2] != ' ':
            return 'win'
        row += 1
    column = 0
    while column <3:
        if grid[0][column] == grid[1][column] == grid[2][column] != ' ':
            return 'win'
        column += 1
    else:
        if grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != ' ':
            return 'win'
        elif ' ' not in grid[0] and ' ' not in grid[1] and ' ' not in grid[2]:
            return 'tie'
        else:
            return False

def printBoard():
    print('  1  2  3 \n  -  -  - \n1| '+grid[0][0]+'| '+grid[0][1]+'| '+grid[0][2]+'|\n  -  -  - \n2| '+grid[1][0]+'| '+grid[1][1]+'| '+grid[1][2]+'|\n  -  -  - \n3| '+grid[2][0]+'| '+grid[2][1]+'| '+grid[2][2]+'|\n  -  -  - ')

print('Hey! Welcome to Tic-Tac-Toe! This game is played by two players.\nPlayer 1 is represented by X and Player 2 by O. Player 1 starts.')
printBoard()
print('This is the grid and it\'s coordinates. The first letter is the row and the second letter the column.\nSo if I want to place your symbol in the upper row in the middle, type \'12\'.')

while True:
    getInput('X')
    sleep(0.3)
    printBoard()
    sleep(0.5)
    if checkForWin() == 'win':
        print('Player 1 (X) has won!')
        break
    elif checkForWin() == 'tie':
        print('You tied!')
        break
    getInput('O')
    sleep(0.3)
    printBoard()
    if checkForWin() == 'win':
        print('Player 1 (O) has won!')
        break
    elif checkForWin() == 'tie':
        print('You tied!')
        break
    sleep(0.5)
