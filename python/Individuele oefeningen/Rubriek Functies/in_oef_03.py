number = int(input("Geef een getal:"))
macht = int(input("Geef een macht:"))

def machtsverheffing(number,macht):
	som = 1
	for i in range(0,macht):
		som = som * number

	return som

print(machtsverheffing(number, macht))

