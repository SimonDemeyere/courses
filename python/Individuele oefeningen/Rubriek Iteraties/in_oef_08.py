getal = int(input("Geef een getal in:"))
getal2 = 1

eString = ""

for i in range(1, getal):
	getal2 = getal2 * 2
	if (getal2 < getal):
		eString = eString + str(getal2) + ","

print(1, eString[:-1])