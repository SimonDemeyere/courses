import string

# kleinAlf = list(string.ascii_lowercase)
kleinAlf = []
grootAlf = []

for i in range(ord('a'), ord('z')+1):
	kleinAlf.append(chr(i))

for i in range(0,26):
	grootAlf.append(kleinAlf[i])

grootAlf = [x.upper() for x in kleinAlf]

print(kleinAlf)
print(grootAlf)