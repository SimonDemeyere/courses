import random

arr1 = []
arr2 = []
arr3 = []

for i in range(0,11):
	arr1.append(random.randint(1, 21)*3)
	arr2.append(random.randint(1, 15)*3)
	arr3.append(arr1[i] + arr2[i])

	print(arr1[i], "+", arr2[i], "=", arr3[i])