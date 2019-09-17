listOfNumbers = ""

for i in range(1, 100):
	if(i < 10):
		listOfNumbers = listOfNumbers + str(0) + str(i) + ","
	elif(i == 99):
		listOfNumbers = listOfNumbers + str(i)
	else:
		listOfNumbers = listOfNumbers + str(i) + ","

print(listOfNumbers)