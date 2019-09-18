number = 0
som = 0

while number >= 0:
	som += number
	number = int(input("Geef een positief getal:"))
	if (number <= 0):
		print(som)
