input = "A man, a plan, a canal, Panama"
forwards = []
backwards = []
for letter in input:
    forwards.append(input[enumerate(letter)])
for letter in input:
    backwards.append(input[enumerate(letter)])
for letter in forwards:
    if forwards[letter] == backwards[letter]: 
        count = count + 1
        if count >= len(forwards):
            print("tHIS IS A PALINDROME")
    else:
        break