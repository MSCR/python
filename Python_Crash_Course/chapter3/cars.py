cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print("\n\n")

cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)
print("Here is the reverse sorted list:")
print(sorted(cars,reverse=True))

cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

print(len(cars))

cars = ['bmw','audi','toyota','subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())