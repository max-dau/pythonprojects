print('Hey! Welcome to Tic-Tac-Toe! This game is played by two players.\nPlayer 1 is represented by X and Player 2 by O.')
print('  1  2  3 \n  -  -  - \nA|  |  |  |\n  -  -  - \nB|  |  |  |\n  -  -  - \nC|  |  |  |\n  -  -  - ')
print('This is the and it\'s coordinates. The letter is the first coordinate and the number is the second coordinate.\nSo if I want to place my symbol in the upper right corner, I type \'A1\'.')

viableX = ['A', 'B', 'C']
viableY = ['1', '2', '3']

#function to get player input as a coordinate and check whether it will work with the program
def getInputAndCheck():
    print('Where do you want to place your symbol?')
    while True:
        coord = input('Where do you want to place your X?\n')

        if coord[0] not in viableX or coord[1] not in viableY:
            print('Your input seems to be illogical. Please try again.')
            continue
        else:
            break

#All lines get filled with "-" for empty at the beginning
A = ['-', '-', '-']
B = ['-', '-', '-']
C = ['-', '-', '-']

#Checks the board for a win, takes every symbol and tests for a line going horizontal, vertical, or across
def checkForWin():
    while True:
