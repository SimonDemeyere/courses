import random

colors = ['groen', 'geel', 'rood', 'paars', 'blauw', 'wit', 'zwart']
randColors = []

# print(randColors.append(random.choice(colors)))
# print(colors, randColors)

def gen_rand_colors():
	for i in range(0,4):
		randColors.append(random.choice(colors[i]))
		# randColors.append(random.choice(colors))
		print(randColors[i])

print(gen_rand_colors())

# for i in range(0,12):
# 	try1 = input("kleur 1:")
# 	try2 = input("kleur 2:")
# 	try3 = input("kleur 3:")
# 	try4 = input("kleur 4:")
