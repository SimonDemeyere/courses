getal = int(input("Geef een getal:"))

faculteit = 1
for i in range(1, getal +1):
	faculteit *= i

print(faculteit)