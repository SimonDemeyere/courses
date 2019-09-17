getal = int(input("Geef een getal"))

if (getal > 2):
	for i in range(2, getal):
		if (getal % i == 0):
			print(getal,"is not a prime number")
           	print(i,"times",getal//i,"is",getal)
           	break
	else:
		print(getal)
else:
   print(getal,"is not a prime number")