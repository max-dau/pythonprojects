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
        global row
        row = int(input('Out of which row would you like to take a match? (input number)\n'))
        if row > 4 or row <= 0:
            print('There only are 4 rows. Choose another one.')
        elif rows[row-1] == 0:
            print('There\'s nothing in this row. Choose another one.')
        else:
            break
    while True:
        global amount
        amount = int(input('How many matches would you like to take out of this row?\n'))
        if amount > rows[row-1]:
            print('This is a higher number than there are matches in this row. Choose another amount\n')
        elif amount == 0:
            print('You can\'t take zero matches out of a row.')
        else:
            break

#computerChoice goups the rows into groups of 4, 2 and 1 matches and chooses on which matches from which row to get rid of
#in order to "balance" the board. a balanced board is a board, which always has
def computerChoice():
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
        print(groups)

def updateRows():
    rows[row-1] -= amount

#prints the entire board.
def printboard():
    print('')
