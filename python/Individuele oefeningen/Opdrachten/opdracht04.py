letter = ord(input("Geef een letter in:").upper())

s = ''
count = letter


for i in range(65, count + 1):
	print(chr(letter))
	s += 'A'
	print(s)
	letter -= 1