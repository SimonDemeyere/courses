number = int(input("Geef een getal:"))

i = 1
hulp = ""

while (i <= number):
	if (i % 10 == 0):
		hulp += " ,"
		i += 1
	else:
		hulp += str(i) + ","
		i += 1
		if (i % 3 == 0):
			hulp += str(i) + ","
print(hulp)