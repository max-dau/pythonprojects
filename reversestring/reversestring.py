string = input('Input a string that you would like to reverse.')

reversedString = ''

index = len(string) - 1
while index >= 0:
    reversedString += string[index]
    index -= 1

print(reversedString)
