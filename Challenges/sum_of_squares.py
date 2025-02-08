# HARD LEVEL

number = int(input ("Give me a number "))
total = 0

for i in range(1, number + 1):
	square = i ** 2
	total = total + square

print (f"the sum of squares of {number} is {total}")