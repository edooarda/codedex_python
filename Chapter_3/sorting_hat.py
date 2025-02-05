gryff = 0
raven = 0
slyth = 0
huffle = 0

print("Welcome to the Sorting Hat Quiz")
print("To discover what is your Hogwarts house")
print("Answer some questions to the Hat")
print("Ready?!\n")

print("Q1) Do you like Dawn or Dusk?")
print("  1) Dawn")
print("  2) Dusk")

answer1 = int(input("Enter your answer (1 - 2): "))

if answer1 == 1:
	gryff = gryff + 1
	raven = raven + 1
elif answer1 == 2:
	slyth = slyth + 1
	huffle = huffle + 1
else:
	print("Wrong Input, choose 1 or 2")

print("Q2) When I’m dead, I want people to remember me as:")
print("  1) The Good")
print("  2) The Great")
print("  3) The Wise")
print("  4) The Bold")

answer2 = int(input("Enter your answer (1-4): "))

if answer2 == 1:
	huffle = huffle + 2
elif answer2 == 2:
	slyth = huffle + 2
elif answer2 == 3:
	raven = raven + 2
elif answer2 == 4:
	gryff = gryff + 2
else:
	print ("Wrong Input")


print("Q3) Which kind of instrument most pleases your ear?")
print( "  1) The violin")
print("  2) The trumpet")
print("  3) The piano")
print("  4) The drum")

answer3 = int(input("Enter your answer (1-4): "))

if answer3 == 1:
	huffle = huffle + 4
elif answer3 == 2:
	slyth = huffle + 4
elif answer3 == 3:
	raven = raven + 4
elif answer3 == 4:
	gryff = gryff + 4
else:
	print ("Wrong Input")

if gryff + raven + slyth + huffle > 0:
	print("----------------------------------------")
	print("Thank you! Your score in which house is:")
	print("🦁 Gryffindor --", gryff)
	print("🦅 Ravenclaw --", raven)
	print("🐍 Slytherin --", slyth)
	print("🦡 Hufflepuff --", huffle)
	print("---------------------------------------\n")
	if gryff >= raven and gryff >= slyth and gryff >= huffle:
		print("Your House is: GRYFFINDOR")
	if raven >= gryff and raven >= slyth and raven >= huffle:
		print("Your House is: RAVENCLAW")
	if slyth >= gryff and slyth >= raven and slyth >= huffle:
		print("Your House is: SLYTHERIN")
	if huffle >= gryff and huffle >= raven and huffle >= slyth:
		print("Your House is: HUFFLEPUFF")
else:
	print("Nothing to show")


# if not(gryff or raven or slyth or huffle): # guard clause, verify first the exit condition
# 	print("Nothing to show")
# 	exit(0)



