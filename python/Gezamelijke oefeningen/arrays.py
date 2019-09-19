reeksGetallen = []
som = 0
aantalGetallen = int(input("Aantal getallen:"))

for i in range(0, aantalGetallen):
	reeksGetallen.append(int(input("Getal:")))

print(reeksGetallen)
print(reeksGetallen[2])

for i in range(0, aantalGetallen):
	som += reeksGetallen[i]

print("De som van de getallen is:", som)