places = ['Tokio','Austin,TX','Amsterdam','Dusseldorf','France']
print(f"My favorite places:\n{places}")

print(f"My favorite places ordered:\n{sorted(places)}")

print(f"My favorite places:\n{places}")

places.reverse()
print(f"My favorite places ordered reverse:\n{places}")

places.reverse()
print(f"My favorite places ordered reverse again:\n{places}")

places.sort()
print(f"My favorite places ordered:\n{places}")

places.sort(reverse=True)
print(f"My favorite places ordered:\n{places}")
