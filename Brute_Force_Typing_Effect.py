
import string
import random
import time
import sys

target = "hello world"
result = ""
alphabeta = string.ascii_lowercase + " "  # Include space since "hello world" has spaces

for target_char in target:
    while True:
        l = random.choice(alphabeta)  # Use random.choice to select a random character
        sys.stdout.write('\r' + result + l)
        sys.stdout.flush()
        if l == target_char:  # Compare to the target character, not the whole target string
            result += l
            break
        time.sleep(0.01)

