#when asked how many sheep he has, a shepherd answers: "somewhere between 700 and 800. if i grozup them into groups of 8, 12, and 15, ther always are 7 left."
#how many sheep does he have?

for x in range(700,800):
    if x%8 == 7 and x%12 == 7 and x%15 == 7:
        print(x)
