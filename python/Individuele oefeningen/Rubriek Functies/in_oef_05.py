word = input("Geef een woord:")

def palindroom(word):
	if(word == word[::-1]):
		# print(word, "is een palindroom.")
		return word + "is een palindroom."
	else:
		# print(word, "is geen palindroom.")
		return word + "is geen palindroom."

print(palindroom(word))