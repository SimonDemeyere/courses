# Oefening 2

leeftijdGebruiker = int(input("Geef je leeftijd in:"))
aantalBulletinVakjes = 0

if (leeftijdGebruiker >= 18):
	print("Je bent ", leeftijdGebruiker, " jaar oud. Je mag deelnemen aan de spelen van de Nationale Loterij.")
	aantalBulletinVakjes = int(input("Wilt u een bulletin van 2, 4, 6, 8, 10 of 12 vakjes?"))
	if (aantalBulletinVakjes == 2):
		print("U hebt gekozen voor ", aantalBulletinVakjes , " vakjes. De kostprijs bedraagt 4 euro.")
	elif (aantalBulletinVakjes == 4):
		print("U hebt gekozen voor ", aantalBulletinVakjes , " vakjes. De kostprijs bedraagt 8 euro.")
	elif (aantalBulletinVakjes == 6):
		print("U hebt gekozen voor ", aantalBulletinVakjes , " vakjes. De kostprijs bedraagt 12 euro.")
	elif (aantalBulletinVakjes == 8):
		print("U hebt gekozen voor ", aantalBulletinVakjes , " vakjes. De kostprijs bedraagt 16 euro.")
	elif (aantalBulletinVakjes == 10):
		print("U hebt gekozen voor ", aantalBulletinVakjes , " vakjes. De kostprijs bedraagt 18 euro.")
	elif (aantalBulletinVakjes == 12):
		print("U hebt gekozen voor ", aantalBulletinVakjes , " vakjes. De kostprijs bedraagt 20 euro.")
	else:
		print("U hebt een ongeldig aantal vakjes gekozen.")
else:
	print("Om  deel  te  nemen  aan  de  spelen  van  de Nationale Loterij moet je minimum 18 jaar oud zijn.")

