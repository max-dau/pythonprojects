input = input('Enter the text you would like to have checked for being a palindrome.\n')

index = 0
palindrome = True
while index < len(input)/2:
    if input[index] != input[len(input)-1-index]:
        palindrome = False
        break
    index += 1

if palindrome == True:
    print('The word you entered is a palindrome.')
else:
    print('The word you entered is not a palindrome.')
