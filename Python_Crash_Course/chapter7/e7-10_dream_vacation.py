active = True
places = {}

while active:
    name = input("Hi, what's your name? ")
    place = input(f"{name.title()}, if you could visit one place in the world, where would you go? ")

    places[name] = place

    response = input("Do you want to continue with the poll? (yes/no) ")
    if response == 'no':
        active = False

print("\nPoll was finishe. These are the responses.\n")
for name,place in places.items():
    print(f"{name.title()} wants to visit {place.title()}")