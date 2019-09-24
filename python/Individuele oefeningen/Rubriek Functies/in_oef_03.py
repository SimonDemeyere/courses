number = int(input("Geef een getal:"))
macht = int(input("Geef een macht:"))

def macht(number,macht):
	som = 1
	for i in range(0,macht):
		som = som * number

	return som

print(macht(number, macht))

