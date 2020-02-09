from time import sleep
import random

inputs = True
password = ''
lettersoptions = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbersoptions = '0123456789'

while inputs == True:
    passwordLength = int(input('How many characters do you want your password to have?'))
    numbersAmount = int(input('How many numbers do you want your password to have?'))
    lettersAmount = int(input('How many letters do you want your password to have?'))

    if lettersAmount + numbersAmount != passwordLength:
        print('Your inputs dont add up. Lets restart.')
        sleep(1)
    else:
        print('Okay. Your password is generating.')
        sleep(1)
        inputs = False

while len(password) < passwordLength:
    newchar = ''
    numbers = sum(c.isdigit() for c in password)
    letters = sum(c.isalpha() for c in password)
    if numbers < numbersAmount and letters < lettersAmount:
        gen = random.randint(0,1)
        if gen == 0:
            newchar = random.choice(lettersoptions)
        elif gen == 1:
            newchar = random.choice(numbersoptions)
    elif numbers < numbersAmount:
        newchar = random.choice(numbersoptions)
    elif letters < lettersAmount:
        newchar =  random.choice(lettersoptions)
    password = password + newchar

print('Your password is: ' + password)
