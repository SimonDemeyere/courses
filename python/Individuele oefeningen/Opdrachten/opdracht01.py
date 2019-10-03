import random

number = int(input("Geef een eindgetal:"))
count = int(input("Hoeveel getallen dien ik te genereren:"))

randArr = []
sortedArr = []
<<<<<<< HEAD
=======

def sortArr(arr):
	arr.sort()
	return arr
>>>>>>> d9b9dba6e13d113db29c57ae8ca442e1d8dec46e

for i in range(0, count):
	randArr.append(random.randint(0, number))

sortedArr = randArr

print("gegenereerde getallen:", randArr)
print("Gesorteerde getallen:", sortArr(sortedArr))