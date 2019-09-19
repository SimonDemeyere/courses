number = int(input("Geef het aantal nummers:"))

string = ""
som = 0
i = 1

# for i in range(1, number +1):
# 	string = "Getal " + str(i) + ": "
# 	count = int(input(string))
# 	som += count

while (i <= number):
	string = "Getal " + str(i) + ": "
	count = int(input(string))
	som += count
	i += 1

gemiddelde = som / number

print("De totale som van ", number, "getallen is ", som, ".")
print("Het gemiddelde van de ", number, "is ", gemiddelde)