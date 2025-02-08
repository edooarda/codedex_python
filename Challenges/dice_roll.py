# MEDIUM LEVEL

import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

total = dice1 + dice2
answer = int(input("What is the total (2-12)? "))

while answer != total:
	answer = int(input("What is the total (2-12)? "))

print("You got it!")