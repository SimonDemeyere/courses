startNumber = int(input("Geef een begin getal:"))
endNumber = int(input("Geef een eind getal:"))

for i in range(startNumber, endNumber + 1):
	# print(startNumber * i)
	if (i <= 3):
		print(startNumber, " x ", i, " = ", startNumber * i, ",")
	elif (i <= 6):
		print(startNumber, " x ", i, " = ", startNumber * i, ",")
	elif (i <= 9):
		print(startNumber, " x ", i, " = ", startNumber * i, ",")
	else:
		print(startNumber, " x ", i, " = ", startNumber * i, ",")