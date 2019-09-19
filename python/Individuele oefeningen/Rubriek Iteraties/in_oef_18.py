import random

number = int(input("Geef een getal:"))

randomNumber = int(random.randint(1, number))

print(randomNumber)

while (number != randomNumber):
	number = int(input("Geef een getal"))
	print(number)

print("Gefiliciteerd, het getal was ", number)