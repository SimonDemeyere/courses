number1 = int(input("Getal 1:"))
number2 = int(input("Getal 2:"))

hulp = 0
for i in range(1, number1):
	if (number1 % i == 0 and number2 % i == 0):
		hulp = i

print("ggd is:", hulp)
