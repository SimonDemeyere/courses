#Opdracht 4

letter = ord(input("Geef een letter in:").upper())

s = ''
count = letter

for i in range(65, count + 2):
	s += chr(i)
for i in range(0, len(s)):
	print(s[:-i])