# hex = [1,2,3,4,5,6,7,8,9,A10,B11,C12,D13,E14,F15]
hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

number = int(input("Geef een getal:"))

# def dec_to_hex(number):
# 	count = None
# 	if (number > 16):
# 		count = int(number / 16)

# 	rest = number % 16

# 	if count is None:
# 		return hex[rest]

# 	else:
# 		return str(hex[count]) + str(hex[rest])	

# print(dec_to_hex(number))

def dec_to_hex(number):
	rest = int(number % 16)
	while number > 16:
		count = int(number / 16)
		print(count)
		


	return count, hex[rest]

print(dec_to_hex(number))
