from time import sleep

rows = [1, 3, 5, 7]
groups = [
    [],
    [],
    [],
    []
]

#userChoice lets the user choose which row and how many matches he wants to take out of the row and checks the inputs.
#Continues for as long as it takes the user to get the input right.
def userChoice():
    while True:
        global rowChoice
        rowChoice = int(input('Out of which row would you like to take a match? (input number)\n')) - 1
        if rowChoice > 3 or rowChoice < 0:
            print('There only are 4 rows. Choose another one.')
        elif rows[rowChoice-1] == 0:
            print('There\'s nothing in this row. Choose another one.')
        else:
            break
    while True:
        global amount
        amount = int(input('How many matches would you like to take out of this row?\n'))
        if amount > rows[rowChoice-1]:
            print('This is a higher number than there are matches in this row. Choose another amount\n')
        elif amount == 0:
            print('You can\'t take zero matches out of a row.')
        else:
            break

#computerChoice first checks, if the computer is within striking distance of winning, if yes does accordingly
#if not groups the rows into groups of 4, 2 and 1 matches and chooses on which matches from which row to get rid of
#in order to "balance" the board. a balanced board is a board, which always has
def computerChoice():
    filledRows = []
    row = 0
    for i in rows:
        if i > 0:
            filledRows.append(i)
        row += 1
    if len(filledRows) == 2 and rows[filledRows[0]] == 1:
        amount = rows[filledRows[1]]
    elif len(filledRows) == 2 and rows[filledRows[1]] == 1:
        amount = rows[filledRows[0]]
    else:
        index = 0
        for i in rows:
            matchesLeft = i
            while matchesLeft > 0:
                if matchesLeft >= 4:
                    groups[index].append(4)
                    matchesLeft -= 4
                elif matchesLeft >= 2:
                    groups[index].append(2)
                    matchesLeft -= 2
                elif matchesLeft == 1:
                    groups[index].append(1)
                    matchesLeft -= 1
            index += 1

#checks the balance of the board and chooses amount and row based on it
        if sum(x.count(4) for x in groups) % 2 != 0:
            row = 0
            for i in rows:
                if 4 in groups[row]:
                    rowChoice = row
                    amount = 4
                    break
                row += 1
        elif sum(x.count(2) for x in groups) % 2 != 0:
            row = 0
            for i in rows:
                if 2 in groups[row]:
                    rowChoice = row
                    amount = 2
                    break
                row += 1
        elif sum(x.count(1) for x in groups) % 2 != 0:
            row = 0
            for i in rows:
                if 1 in groups[row]:
                    print('row: ' + str(row))
                    rowChoice = row
                    print('rowChoice:' + str(rowChoice))
                    amount = 1
                    break
                row += 1

def updateRows():
    print('new amount: ' + str(rows[rowChoice] - amount) + '\nin row ' + str(rowChoice))
    rows[rowChoice] -= amount

#prints the entire board.
def printBoard():
    print('This is the board right now.')
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

while True:
    printBoard()
    userChoice()
    updateRows()
    if checkWin() == True:
        print('The computer has won.')
        break
    printBoard()
    sleep(1.5)
    computerChoice()
    updateRows()
    if checkWin() == True:
        print('The computer has won.')
        break
