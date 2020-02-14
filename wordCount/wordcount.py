input = input('Enter the text of which you would like to have the words counted.')

words = 0
index = 0
while index < len(input)-1:
    if input[index] == ' ':
        words += 1
    index += 1

print(words+1)
