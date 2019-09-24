# w = int(input("Geef breedte:"))
# h = int(input("Geef hoogte:"))

# def om_vk(w):
# 	print("Omtrek van een vierkant:", w, "x 4 =", w*4)

# def opp_vk(w, h):
# 	print("Oppervlakte vierkant:", w, "² =", w**2)

# # w = int(input("Geef breedte:"))
# # h = int(input("Geef hoogte:"))

# def om_rh(w, h):
# 	print("Omtrek van een rechthoek: (", w, "+", h, ") x 2 =", (w+h)*2)

# def opp_rh(w, h):
# 	print("Oppervlakte van een rechthoek:", w, "*", h, "=", w*h)

# # w = int(input("Geef lengte zijde:"))
# # h = int(input("Geef hoogte:"))

# def om_ruit(w):
# 	print("omtrek van een ruit:", w, "* 4", "=", w*4)

# def opp_ruit(w):
# 	print("omtrek van een ruit:", w, "* 4", "=", w*4)

# om_vk(w)
# opp_vk(w,h)
# om_rh(w,h)
# opp_rh(w,h)
# om_ruit(w)


# Omtrek van een ruit
# Oppervlakte van een ruit
# Omtrek van een driehoek
# Oppervlakte van een driehoek
# Omtrek van een parallellogram
# Oppervlakte van een parallelogram
# Omtrek van een cirkel
# Oppervlakte van een cirkel

import math

def omtrekVierkant(zijde):
	return zijde * 4

def opperVlakteVierkant(zijde):
	return zijde * zijde

def omtrekRechthoek(lengte, breedte):
	return (lengte + breedte)*2

def oppervlakteRechthoek(lengte, breedte):
	return (lengte * breedte)

def omtrekRuit(zijde):
	return zijde * 4

def oppervlakteRuit(basis, hoogte):
	return basis * hoogte

def omtrekGelijkzijdigeDriehoek(zijde):
	return 3 * zijde

def oppervlakteGelijkzijdigeDriehoek(basis,hoogte):
	return (basis * hoogte)/2

def omtrekParallellogram(basis,zijde):
	return (basis + zijde) * 2

def oppervlakteParallellogram(basis,hoogte):
	return (basis * hoogte)

def omtrekCirkel(straal):
	return (2 * math.pi * straal)

def oppervlakteCirkel(straal):
	return math.pi * straal * straal

keuze=0

print("__________________________________________________")
print("")
print("MENU")
print("__________________________________________________")
print("1. Omtrek van een vierkant berekenen")
print("2. Oppervlakte van een vierkant berekenen")
print("3. Omtrek van een rechthoek berekenen")
print("4. Oppervlakte van een rechthoek berekenen")
print("5. Omtrek van een ruit berekenen")
print("6. Oppervlakte van een ruit berekenen")
print("7. Omtrek van een gelijkzijdige driehoek berekenen")
print("8. Oppervlakte van een driehoek berekenen")
print("9. Omtrek van een parallellogram berekenen")
print("10. Oppervlakte van een parallellogram berekenen")
print("11. Omtrek van een cirkel berekenen")
print("12. Oppervlakte van een cirkel berekenen")
print("__________________________________________________")

keuze=int(input("Geef uw keuzecijfer in:"))

if(keuze == 1):

	print("-----------------------------------")
	print("Bereken de omtrek van een vierkant")
	print("-----------------------------------")

	resultaat = omtrekVierkant(int(input("Bereken de omtrek van een vierkant. Geef één zijde in: ")))

	print("De omtrek van het vierkant is:",resultaat)
	
elif(keuze == 2):

	print("-----------------------------------")
	print("Bereken de oppervlakte van een vierkant")
	print("-----------------------------------")

	resultaat = opperVlakteVierkant(int(input("Bereken de oppervlakte van een vierkant. Geef één zijde in: ")))

	print("De oppervlakte van het vierkant is:",resultaat)

elif(keuze == 3):

	print("-----------------------------------")
	print("Bereken de omtrek van een rechthoek")
	print("-----------------------------------")

	lengte=int(input("Geef de lengte in:"))
	breedte=int(input("Geef de breedte in:"))
	resultaat = omtrekRechthoek(lengte,breedte)

	print("De omtrek van het rechthoek is:",resultaat)

elif(keuze == 4):

	print("-----------------------------------")
	print("Bereken de oppervlakte van een rechthoek")
	print("-----------------------------------")

	lengte=int(input("Geef de lengte in:"))
	breedte=int(input("Geef de breedte in:"))
	resultaat = oppervlakteRechthoek(lengte,breedte)

	print("De oppervlakte van het rechthoek is:",resultaat)

elif(keuze == 5):

	print("-----------------------------------")
	print("Bereken de omtrek van een ruit")
	print("-----------------------------------")

	resultaat = omtrekRuit(int(input("Bereken de omtrek van een ruit. Geef één zijde in: ")))

	print("De omtrek van het vierkant is:",resultaat)

elif(keuze == 6):

	print("-----------------------------------")
	print("Bereken de oppervlakte van een ruit")
	print("-----------------------------------")

	basis=int(input("Geef de basis in:"))
	hoogte=int(input("Geef de hoogte in:"))
	resultaat = oppervlakteRuit(basis,hoogte)

	print("De oppervlakte van het ruit is:",resultaat)

elif(keuze == 7):

	print("-----------------------------------")
	print("Bereken de omtrek van een gelijkzijdige driehoek")
	print("-----------------------------------")

	resultaat = omtrekGelijkzijdigeDriehoek(int(input("Bereken de omtrek van een gelijkzidige driehoek. Geef één zijde in: ")))

	print("De omtrek van een gelijzijdige driehoek is:",resultaat)

elif(keuze == 8):

	print("-----------------------------------")
	print("Bereken de oppervlakte van een gelijkzijdige driehoek")
	print("-----------------------------------")

	basis=int(input("Geef de basis in:"))
	hoogte=int(input("Geef de hoogte in:"))
	resultaat = oppervlakteGelijkzijdigeDriehoek(basis,hoogte)

	print("De oppervlakte van het gelijkzidige driehoek is:",resultaat)

elif(keuze == 9):

	print("-----------------------------------")
	print("Bereken de omtrek van een parallellogram")
	print("-----------------------------------")
	basis=int(input("Geef de basis in:"))
	zijde=int(input("Geef de zijde in:"))

	resultaat = omtrekParallellogram(basis,zijde)

	print("De oppervlakte van een parallellogram is:",resultaat)

elif(keuze == 10):

	print("-----------------------------------")
	print("Bereken de oppervlakte van een parallellogram")
	print("-----------------------------------")

	basis=int(input("Geef de basis in:"))
	hoogte=int(input("Geef de hoogte in:"))
	resultaat = opppervlakteParallellogram(basis,hoogte)

	print("De oppervlakte van een parallellogram is:",resultaat)

elif(keuze == 11):

	print("-----------------------------------")
	print("Bereken de omtrek van een cirkel")
	print("-----------------------------------")

	straal=int(input("Geef de straal in:"))
	resultaat = omtrekCirkel(straal)

	print("De omtrek van een cirkel is:",resultaat)

elif(keuze == 12):

	print("-----------------------------------")
	print("Bereken de oppervlakte van een cirkel")
	print("-----------------------------------")

	straal=int(input("Geef de straal in:"))
	resultaat = oppervlakteCirkel(straal)
	print("De oppervlakte van een cirkel is:",resultaat)
	
