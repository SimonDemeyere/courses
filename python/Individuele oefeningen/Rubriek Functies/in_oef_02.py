year = int(input("Geef jaartal"))

# def checkSchrikkeljaar(year):
# 	if (year % 4 == 0):
# 		print(year, "is een schrikkeljaar")
# 	if (year % 400 == 0):
# 		print(year, "is een schrikkeljaar")
			
# checkSchrikkeljaar(year)

def leap_year(year):
	if (year % 4 == 0):
		if (year % 100 == 0):
			if(year % 400 == 0):
				print(year, "is een schrikkeljaar")
			else:
				print(year, "is geen schrikkeljaar")
		else:
			print(year, "is een schrikkeljaar")
	else:
		print(year, "is geen schrikkeljaar")

leap_year(year)