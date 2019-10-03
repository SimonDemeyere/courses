#Opdracht 1

import random

number = int(input("Geef een eindgetal:"))
count = int(input("Hoeveel getallen dien ik te genereren:"))

randArr = []
sortedArr = []

def sortArr(arr):
	arr.sort()
	return arr

for i in range(0, count):
	randArr.append(random.randint(0, number))

sortedArr = randArr

print("gegenereerde getallen:", randArr)
print("Gesorteerde getallen:", sortArr(sortedArr))