favorite_places = {
    'manuel':['japan', 'germany','united states'],
    'dinorha':['japan'],
    'aaron':['china', 'russia'],
}

for person,places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{person.title()}'s favorite places are:")
    else:
        print(f"\n{person.title()}'s favorite place is:")
    for place in places:
        print(f"{place.title()}")