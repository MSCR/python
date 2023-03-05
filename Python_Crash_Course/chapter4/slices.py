players = ['charles','martina','michael','florence','eli','aaron','dinorha','alexis','dario']
print(players)

print(players[1:3])
print(players[:3])
print(players[1:])
print(players[-3:])

print("The first three items in the list are:")
for player in players[:3]:
	print(player.title())

print("Three items from the middle of the list are:")
for player in players[3:-3]:
	print(player.title())

print("The last three items of the list are:")
for player in players[-3:]:
	print(player.title())