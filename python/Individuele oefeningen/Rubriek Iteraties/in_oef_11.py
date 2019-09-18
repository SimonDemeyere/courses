userNumber = int(input("Geef aantal:"))
startNumber = 0

number1 = 0
number2 = 1

print(startNumber)
for i in range(1, userNumber):
	som = number1 + number2
	number1 = number2
	number2 = som

	print(som)