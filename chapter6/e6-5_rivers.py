rivers = {
    'nile':'egipt',
    'mississippi':'usa',
    'lerma':'mexico'
}

for river,country in rivers.items():
    print(f"The {river.title()} runs throught {country.title()}.")

print("\nThese are the rivers mentioned")
for river in rivers.keys():
    print(river.title())

print("\nThese are the countries mentioned")
for river in rivers.values():
    print(river.title())