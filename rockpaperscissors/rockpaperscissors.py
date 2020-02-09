from random import randrange
from time import sleep

draw = 0
playerwin = 0
computerwin = 0

print('Hi! Lets play a game of rock, paper, scissors!')
start = input('yes or no?')

while start == 'yes':
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    sleep(1)

    # rock = 1, paper = 2, scissors = 3
    moves = [
        'rock',
        'paper',
        'scissors'
    ]

    #gets players move and converts it to number
    movePlayer = input('Whats your move? rock, paper, scissors')
    movePlayer = int(moves.index(movePlayer))

    #randomly generates computer move and prints it as a word
    moveComputer = randrange(0,2)
    print('The computer chose ' + moves[moveComputer])
    sleep(0.5)

    #applies rules and figures out who won
    if movePlayer == 0:
        if moveComputer == 0:
            print('Draw!')
            draw += 1
        elif moveComputer == 1:
            print ('The computer won!')
            computerwin += 1
        elif moveComputer == 2:
            print('You won!')
            playerwin += 1

    elif movePlayer == 1:
        if moveComputer == 0:
            print('You won!')
            playerwin += 1
        elif moveComputer == 1:
            print('Draw!')
            draw += 1
        elif moveComputer == 2:
            print('The computer won!')
            computerwin += 1

    elif movePlayer == 2:
        if moveComputer == 0:
            print('The computer won!')
            computerwin += 1
        elif moveComputer == 1:
            print('You won!')
            playerwin += 1
        elif moveComputer == 2:
            print('Draw!')
            draw += 1

    else:
        print('You seem to have given a falsy input.')

    start = input('Do you want to play another round?')

print('Overall, you have won ' + str(playerwin) + ' times, the computer won ' + str(computerwin) + ' times and you drew ' + str(draw) + ' times.')

sleep(0.5)

if playerwin<computerwin:
    print('So overall, you lost.')

elif playerwin>computerwin:
    print('So overall, you won.')

else:
    print('So overall, you drew.')
