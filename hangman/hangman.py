import random
wrongguesses = 0
guesses = 0

print('Hey! Lets play a game of hangman.\nThe computer will now generate a random word and you will guess it\'s letters.\nYou have a total of 6 guesses before you lose.\nFor every right letter, the computer will show you one instance of it occuring in the word.' )

with open('sowpods.txt') as f:
	words = list(f)
word = random.choice(words).strip()
print(word)

maskedword = ''
for letter in word:
    maskedword = maskedword + '_'

print('This is the masked word: ' + maskedword + '. It has ' + str(len(maskedword)) + ' letters.')

while True:
    guess = input('Guess a letter!')
    guesses += 1

    if guess in word:
        print('You guessed right!')
        index = word.find(guess)
        maskedword = maskedword[:index] + guess + maskedword[index+1:]
        word = word[:index] + '-' + word[index+1:]
        print(maskedword)

        if '_' not in maskedword:
            print('You figured out the whole word! You won. This took you ' + str(wrongguesses) + ' wrong guesses. Congratulations!')
            break
    else:
        print('Your guess was wrong.')
        wrongguesses += 1
        print('Take another guess.')

    print('You guessed wrongly ' + str(wrongguesses) + ' times now. That means that you have ' + str(6 - wrongguesses) + ' wrong guesses left before you lose.')

    if wrongguesses == 6:
        print('You have used up all of you guesses and couldn\'t figure it out. You lost.')
        break
