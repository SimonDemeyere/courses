# number = int(input("Hoeveel getallen wilt u ingeven?:"))
# s = ""

# for i in range(0, number):
# 	s = int(input("Geef getal" + str(i+1) + ": "))

arr = [1, 3, 30, 202, 7, 31, 25, 14, 8]
total = 0

def maximum(arr):
	print(max(arr))

def minimum(arr):
	print(min(arr))

def count_char(arr):
	for i in arr:
		total += len(i)
	return total

q = input("Wil je het 'maximum' of 'minimum' weergeven?:")

if (q == "maximum"):
	maximum(arr)
elif (q == "minimum"):
	minimum(arr)
else:
	print("U kan enkel kiezen tussen maximum of minimum")

# print(count_char(arr))