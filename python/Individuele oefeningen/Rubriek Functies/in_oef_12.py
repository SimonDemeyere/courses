unevenMonth = ["januari", "maart", "mei", "juli", "augustus", "oktober", "december"]
evenMonth = ["april", "juni", "september", "november"]
februari = "februari"
leapYear = ""

userMonth = input("Geef een maand in:")
year = int(input("Geef een jaar in:"))

def leap_year(year):
	if (year % 4 == 0):
		if (year % 100 == 0):
			if(year % 400 == 0):
				leapYear = "true"
				return leapYear
			else:
				leapYear = "false"
				return leapYear
		else:
			leapYear = "true"
			return leapYear
	else:
		leapYear = "false"
		return leapYear

def days_a_month(month, year):
	i = 0
	days = 0
	for i in range(month == unevenMonth):
		if (month == unevenMonth[i]):
			days = 31
		elif (month == evenMonth[i]):
			days = 30
		else:
			if (leap_year(year) == "true"):
				days = 29
			else:
				days = 28
		print(i)
	print(month, "heeft in het jaar", year, days, "dagen.")

leap_year(year)
days_a_month(userMonth, year)