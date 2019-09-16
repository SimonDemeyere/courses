# Oefening 4

geboorteJaar = int(input("Geef je geboortejaar in:"))
huidigJaar = int(input("Geef het huidige jaartal in:"))

verschilJaartal = huidigJaar - geboorteJaar

if (verschilJaartal <= 0):
	print("Een getal onder 0 is niet mogelijk.")
else:
	if (verschilJaartal >= 18):
		print("Vanaf nu mag, kan en beslis ik alles, binnen de wettelijke grenzen")
	else:
		print("Gelukkig heb ik mijn ouders die alles voor me regelen.")

