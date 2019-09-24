number = int(input("Geef een getal:"))

def dec_to_bin(number):
	print("number:" + str(number))
	if number > 1:
		dec_to_bin(number // 2) 
	print(number % 2, end = '')

dec_to_bin(number)