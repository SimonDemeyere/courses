# hex = [1,2,3,4,5,6,7,8,9,A10,B11,C12,D13,E14,F15]
hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

number = int(input("Geef een getal:"))

def dec_to_hex(number):
	if (0 <= number < 16):
		rest = int(number % 16)
		return hex[rest]
	elif (number < 0):
		return "0"
	else:
		restConverted = ""
		while number > 0:
			rest = int(number % 16)
			restConverted = restConverted + str(hex[rest])
			number = int(number / 16)
		return restConverted[::-1]

print(dec_to_hex(number))
