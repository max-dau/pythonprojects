from random import randrange

randomNumber = randrange(0,20)
print(randomNumber)

guess = input('Guess a number between 0 and 20!')
guess = int(guess)
guesses = 1

while guess!=randomNumber:
	print('Thats wrong.')
	if guess>randomNumber:
		print('Your guess was too high.')
	if guess<randomNumber:
		print('Your guess was too low.')
	guess = input('Take another guess!')
	guess = int(guess)
	guesses += 1

print('Thats right! Congratulations!')
print('This took you ' + str(guesses) + ' guesses.')
