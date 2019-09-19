import random

arr1 = []
arr2 = []
arr3 = []
som1 = 0
som2 = 0

for i in range(0,10):
	arr1.append(random.randint(1, 21)*3)

	if (arr1[i] % 2 == 0):
		arr3.append(arr1[i])
		print("test arr1",arr1[i])
	else:
		som1 += arr1[i]
		print("som1:",som1)

for i in range(0,10):
	arr2.append(random.randint(1, 21)*3)

	if (arr2[i] % 2 == 0):
		arr3.append(arr2[i])
		print("test arr2",arr2[i])
	else:
		som2 += arr2[i]
		print("som1:",som2)


som3 = som1 + som2

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array 3:", arr3)

print("som:", som3)