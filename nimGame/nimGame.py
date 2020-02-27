from time import sleep

rows = [1, 3, 5, 7]

#userChoice lets the user choose which row and how many matches he wants to take out of the row and checks the inputs.
#Continues for as long as it takes the user to get the input right.
def userChoice():
    global userRow
    while True:
        userRow = int(input('Out of which row would you like to take a match? (input number)\n')) - 1
        if userRow > 3 or userRow < 0:
            print('There only are 4 rows. Choose another one.')
        elif rows[userRow] == 0:
            print('There\'s nothing in this row. Choose another one.')
        else:
            break
    global userAmount
    while True:
        userAmount = int(input('How many matches would you like to take out of this row?\n'))
        if userAmount > rows[userRow]:
            print('This is a higher number than there are matches in this row. Choose another amount\n')
        elif userAmount == 0:
            print('You can\'t take zero matches out of a row.')
        else:
            break

#computerChoice first checks, if the computer is within striking distance of winning, if yes does accordingly
#if not groups the rows into groups of 4, 2 and 1 matches and chooses on which matches from which row to get rid of
#in order to "balance" the board. a balanced board is a board, which always has
def computerChoice():
    global computerAmount
    global computerRow
    filledRows = []
    i = 0
    while i < 4:
        if rows[i] > 0:
            filledRows.append(i)
        i += 1
    if len(filledRows) == 2 and rows[filledRows[0]] == 1:
        computerAmount = rows[filledRows[1]]
        computerRow = filledRows[1]
    elif len(filledRows) == 2 and rows[filledRows[1]] == 1:
        computerAmount = rows[filledRows[0]]
        computerRow = filledRows[0]
    elif len(filledRows) == 1:
        if rows[filledRows[0]] == 1:
            computerAmount = 1
        else:
            computerAmount = filledRows[0] - 1
        computerRow = filledRows[0]
    else:
        groups = [
            [],
            [],
            [],
            []
        ]
        i = 0
        for matches in rows:
            while matches > 0:
                if matches >= 4:
                    groups[i].append(4)
                    matches -= 4
                elif matches >= 2:
                    groups[i].append(2)
                    matches -= 2
                elif matches == 1:
                    groups[i].append(1)
                    matches -= 1
            i += 1
#checks the balance of the board and chooses amount and row based on it
        computerAmount = 0
        if sum(x.count(4) for x in groups) % 2 != 0:
            computerAmount += 4
        if sum(x.count(2) for x in groups) % 2 != 0:
            computerAmount += 2
        if sum(x.count(1) for x in groups) % 2 != 0:
            computerAmount += 1

        i = 0
        for row in rows:
            if row >= computerAmount:
                computerRow = i
                break
            i += 1
        else:
#find biggest row and empty it if balancing is impossible
            biggestRow = 0
            for row in rows:
                if rows[biggestRow] < row:
                    biggestRow = rows.index(row)
            computerRow = biggestRow
            computerAmount = rows[biggestRow]
    print('\nThe computer takes ' + str(computerAmount) + ' matches out of row ' + str(computerRow + 1) + '\n')
    sleep(0.5)

#prints the entire board.
def printBoard():
    print('This is the board right now:')
    sleep(0.5)
    row = 0
    while row <= 3:
        outputLine = ''
        for i in range(0, rows[row]):
            outputLine += 'I '
        print(outputLine)
        row += 1

def checkWin():
    empty = 0
    for i in rows:
        if i == 0:
            empty += 1
    if empty == 4:
        return True


printBoard()
while True:
    userChoice()
    rows[userRow] -= userAmount
    printBoard()
    if checkWin() == True:
        print('The computer has won.')
        break
    sleep(1)
    computerChoice()
    rows[computerRow] -= computerAmount
    printBoard()
    if checkWin() == True:
        print('The user has won.')
        break
