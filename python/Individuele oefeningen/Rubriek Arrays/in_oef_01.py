reeksGetallen = []
som = 0
aantalGetallen = int(input("Aantal getallen:"))

for i in range(0, aantalGetallen):
	number = int(input("Geef een positief getal:"))
	if (number >= 0):
		reeksGetallen.append(number)
	else:
		print("U hebt een negatief getal ingegeven.")

for i in range(0, aantalGetallen):
	som += reeksGetallen[i]

print("De som van de getallen is:", som)