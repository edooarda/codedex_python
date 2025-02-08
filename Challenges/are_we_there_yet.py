# EASY LEVEL

answer = input("Are we there yet? ")

while answer.lower() != "yes":
	answer = input("Are we there yet? ")

# while (answer := input("Are we there yet? ").lower()) != "yes": # doing in one line, Nico style
# 	continue

print("Finally!")