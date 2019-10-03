#Opdracht 3

number = int(input("Geef een getal in:"))
count = int(input("Geef het aantal weer te geven getalen in:"))

s = ""

for i in range(1, count + 1):
	number *= i
	s += str(number) + ','

print(s[:-1])