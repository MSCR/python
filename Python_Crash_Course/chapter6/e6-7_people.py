person1 = {
    'first':'manuel',
    'second':'cortes',
    'age':32,
    'city':'pajacuaran',
}

person2 = {
    'first':'dinorha',
    'second':'martinez',
    'age':28,
    'city':'guadalajara',
}

person3 = {
    'first':'aaron',
    'second':'dominguez',
    'age':33,
    'city':'mazatlan',
}

people = [person1, person2, person3]

for person in people:
    full_name = f"{person['first'].title()} {person['second'].title()}"
    city = f"{person['city'].title()}"
    age = person['age']

    print(f"\nFull Name: {full_name}")
    print(f"City: {city}")
    print(f"Age: {age}")