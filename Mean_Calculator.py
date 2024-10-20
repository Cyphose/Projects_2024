complete = False
numbers = []
while not complete:
    entry = input("add the number ")
    if entry != "done":numbers.append(entry)
    else:
        complete = True
total = sum(float(num) for num in numbers)
print(total/len(numbers))