input = input('Enter the word that you would like ot have translated to Piglatin.\n')

vocals = ['A', 'E', 'I', 'O', 'U']
index = 0
while True:
    if input[index].upper() not in vocals:
        firstConsonant = input[index]
        break
    else:
        index += 1

output1 = input[0:index]
output2 = input[index+1:]
output = output1 + output2 + ' - ' + firstConsonant + 'ay'
print(output)
