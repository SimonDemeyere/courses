  
#priemgetallen

getal = int(input("Geef een getal in groter dan nul:"))
afdrukOpscherm=""

for i in range(2, getal):
	for x in range(2, i):
		if i % x == 0:
			break
	else:
		afdrukOpscherm = afdrukOpscherm + str(i) + ","

print(afdrukOpscherm[:-1])