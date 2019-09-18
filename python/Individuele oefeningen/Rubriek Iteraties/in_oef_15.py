number = int(input("Geef het aantal nummers:"))

string = ""
som = 0

for i in range(1, number +1):
	string = "Getal " + str(i) + ": "
	count = int(input(string))
	som += count

# while 

gemiddelde = som / number

print("De totale som van ", number, "getallen is ", som, ".")
print("Het gemiddelde van de ", number, "is ", gemiddelde)