number = int(input("Geef aantal namen:"))
nameList = []

for i in range(0, number):
	nameList.append(input("Geef naam in:"))

print(*nameList, sep = "\n") 