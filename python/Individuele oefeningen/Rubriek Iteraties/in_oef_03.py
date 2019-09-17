getal = int(input("Geef een getal in:"))
# halfGetal = int(getal / 2)
ster = ""

if (getal % 2 == 0):
	for i in range(0,getal,1):
		ster = ster + "*"
		print(ster)

	print(ster)

	for i in range(0,getal,1):
		print(ster[getal:i:-1])
else:
	print("Getal is geen even getal")

