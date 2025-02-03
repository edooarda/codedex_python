ph = int (input("Enter pH between 0 and 14: "))

if ph > 7:
	print("Basic")
elif ph < 7:
	print("Acid")
else:
	print("Neutral")