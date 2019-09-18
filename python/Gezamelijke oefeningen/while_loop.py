som = 0
test = 5
cntlGetal = int(input("Getal?"))

while cntlGetal >= 0 || test == 5:
	som += cntlGetal
	test = int(input("Geef test in:"))
	if cntlGetal < 0:
		print("De som is:", som)