favorite_numbers = {
    'Manuel':[15,12,45],
    'Dinorha':[32,1],
    'Aaron':[12,53,23,12],
    'Miguel':[23,54,35,29,19],
    'Carlos':[23,12],
}

for name,numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"\n{name.title()}'s favorite numbers are:")
    else:
        print(f"\n{name.title()}'s favorite number is:")
    for number in numbers:
        print(number)