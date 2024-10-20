lister = []
i = 0
while len(lister)< 100:
    lister.append(i)
    i = i + 1
for number in lister:
    if number%3 == 0:
        lister[number] = "Fizz"
    elif number%5 == 0:
        lister[number] = "Buzz"
print(lister)