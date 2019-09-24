s = input("Geef een zin:")
editS = s

print(s)
print(s.translate({ord(i): None for i in 'aeiouy'}))