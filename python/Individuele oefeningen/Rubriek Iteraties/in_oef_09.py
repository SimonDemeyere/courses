getal = int(input("Geef een getal"))

print(2)
print(3)
for i in range(3, getal):
	if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
		print(i)