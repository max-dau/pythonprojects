rows = [1, 2, 5, 7]
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
        rowChoice = int(input('Out of which row would you like to take a match? (input number)\n'))
        if rowChoice > 4 or rowChoice <= 0:
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
    for i in rows:
        if rows[i] > 0:
            filledRows.append(i)
    if len(filledRows) == 2:
        if rows[filledRows[0]] == 1:
            amount = rows[filledRows[1]]
        elif rows[filledRows[1]] == 1:
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
        if groups.count(4) % 2 != 0:
            for i in rows:
                if rows[i] >= 4:
                    i = rowChoice
                    amount = 4
                i += 1
        elif groups.count(2) % 2 != 0:
            for i in rows:
                if rows[i] >= 2:
                    i = rowChoice
                    amount = 2
                i += 1
        elif groups.count(1) % 2 != 0:
            for i in rows:
                if rows[i] >= 1:
                    i = rowChoice
                    amount = 1
                i += 1


def updateRows():
    rows[rowChoice-1] -= amount

#prints the entire board.
def printboard():
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
        if rows[i] == 0:
            empty += 1
    if emtpy == 4:
        return True

while True:
    printboard()
    computerChoice()
    updateRows()
    if checkWin() == True:
        print('The computer has won.')
        break
    playerChoice()
    updateRows()
    if checkWin() == True:
        print('The computer has won.')
        break
