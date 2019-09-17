# oefening 1

aantalNummers = int(input("Hoeveel getallen?"))

som = 0
for i in range(aantalNummers):
	testGetal = int(input("Getal " + str(i+1) + ": "))
	som = som + testGetal
 
print(som)

