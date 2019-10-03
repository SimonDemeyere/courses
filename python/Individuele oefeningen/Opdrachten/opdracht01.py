import random

number = int(input("Geef een eindgetal:"))
count = int(input("Hoeveel getallen dien ik te genereren:"))

randArr = []
sortedArr = []

for i in range(0, count):
	randArr.append(random.randint(0,100))

sortedArr = randArr
sortedArr.sort()

print("gegenereerde getallen:", randArr)
print("Gesorteerde getallen:", sortedArr)