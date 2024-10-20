starter_prime_numbers = [3, 5]
current_number = 6

while current_number <= 200:
    is_prime = True
    for prime in starter_prime_numbers:
        if current_number % prime == 0:
            is_prime = False
            break
    if is_prime:
        starter_prime_numbers.append(current_number)
    current_number += 1

print(starter_prime_numbers)
