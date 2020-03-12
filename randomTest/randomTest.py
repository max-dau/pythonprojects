import random

while True:
    lowest = int(input('What should be the lowest possible integer?\n'))
    highest = int(input('\nWhat should be the highest possible integer?\n'))
    if highest > lowest and isinstance(lowest, int) and isinstance(highest, int):
        break
    else:
        print('\nYour input doesn\'t seem to work. Please give another one.\n')

randomNumbers = int(input('\nHow many random numbers do you want to generate?\n'))

amount = []

for i in range(highest-lowest+1):
    amount.append(0)

print('\n')
i = 0
for i in range(randomNumbers):
    number = random.randint(lowest, highest)
    print('Random number generated: ' + str(number))
    amount[number] += 1

print('\n\n\nDone! These are the amounts of numbers printed:')

i = lowest
for element in amount:
    print(str(i) + ': ' + str(element))
    i += 1

lowestAmount = amount[0]
for element in amount:
    if element < lowestAmount:
        lowestAmount = element

highestAmount = amount[0]
for element in amount:
    if element > highestAmount:
        highestAmount = element

if lowestAmount != 0:
    print('There\'s a difference of ' + str(round(highestAmount/lowestAmount*100-100, 1)) + '% between the highest and lowest amount of times a number was generated.')
else:
    print('The lowest amount is 0 and the highest amount is ' + str(highestAmount) + '.')
