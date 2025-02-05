for i in range(1, 101):
	if i % 5 == 0 and i % 3 == 0:
		print ("FizzBuzz")
	elif i % 3 == 0:
		print("FIZZ")
	elif i % 5 == 0:
		print("BUZZ")
	else:
		print(i)


# Usign only one print
# for i in range(1, 101):
# 	txt = ""
# 	if i % 3 == 0:
# 		txt += "Fizz"
# 	if i % 5 == 0:
# 		txt += "Buzz"
# 	if not txt:
# 		txt = str(i)
# 	print(txt)