w = int(input("Geef breedte:"))
h = int(input("Geef hoogte:"))

def om_vk(w):
	print("Omtrek van een vierkant:", w, "x 4 =", w*4)

def opp_vk(w, h):
	print("Oppervlakte vierkant:", w, "² =", w**2)

# w = int(input("Geef breedte:"))
# h = int(input("Geef hoogte:"))

def om_rh(w, h):
	print("Omtrek van een rechthoek: (", w, "+", h, ") x 2 =", (w+h)*2)

def opp_rh(w, h):
	print("Oppervlakte van een rechthoek:", w, "*", h, "=", w*h)

# w = int(input("Geef lengte zijde:"))
# h = int(input("Geef hoogte:"))

def om_ruit(w):
	print("omtrek van een ruit:", w, "* 4", "=", w*4)

def opp_ruit(w):
	print("omtrek van een ruit:", w, "* 4", "=", w*4)

om_vk(w)
opp_vk(w,h)
om_rh(w,h)
opp_rh(w,h)
om_ruit(w)


# Omtrek van een ruit
# Oppervlakte van een ruit
# Omtrek van een driehoek
# Oppervlakte van een driehoek
# Omtrek van een parallellogram
# Oppervlakte van een parallelogram
# Omtrek van een cirkel
# Oppervlakte van een cirkel