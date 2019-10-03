#Opdracht 5

import random

number = int(input("Geef een getal in:"))

arr = []
s = ""

for i in range(0, number):
	s += "(" + str(random.randint(0, 20)) + "," + str(random.randint(0, 20)) + "),"

arr.append(s[:-1])

print("Resultaat:")
print("mijnReeks =", arr)