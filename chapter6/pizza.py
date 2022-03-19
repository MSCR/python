# Let's create some nesting of lists and dictionaries
# Nest a List in a dictionary

# Store information about a pizza being ordered
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# Access an specific element
print(f"Second topping requested: {pizza['toppings'][1]}")