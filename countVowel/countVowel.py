input = input('Enter the text of which you would like to have the vowels counted.')

index = 0
vowelsCount = 0
vowels = ['A', 'E', 'I', 'O', 'U']
while index < len(input):
    if input[index].upper() in vowels:
        vowelsCount += 1
    index += 1

print(vowelsCount)
