pet1 = {
    'name':'kirara',
    'species':'cat',
    'age':4,
}

pet2 = {
    'name':'mumu',
    'species':'cat',
    'age':3,
}

pet3 = {
    'name':'akane',
    'species':'guinea pig',
    'age':5,
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"\nName: {pet['name'].title()}")
    print(f"species: {pet['species'].title()}")
    print(f"Age: {pet['age']}")