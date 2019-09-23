number = int(input("Geef een getal:"))

def machtsverheffing(number):
	som = 1
	for i in range(0,2):
		som = som * number

	return som

def pythagoras(a,b,c):
	# a²=b²+c²
	if (machtsverheffing(int(a)) == machtsverheffing(int(b)) + machtsverheffing(int(c))):
		print(machtsverheffing(int(a)), "=", machtsverheffing(int(b)), "+", machtsverheffing(int(c)))

for x in range(1,number+1):
	for y in range(1,number+1):
		for z in range(1,number+1):
			# if ()
			pythagoras(x,y,z)
