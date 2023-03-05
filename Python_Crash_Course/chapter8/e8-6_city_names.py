def city_country(city,country):
    """This function returns the city and country in one string"""
    return f"{city.title()}, {country.title()}"

place = city_country("guadalajara","mexico")
print(place)

place = city_country("tokio","japan")
print(place)

place = city_country("Essen","germany")
print(place)