toppings = []
prompt = "\nPlease tell us which topping do you want for your pizza: "
prompt += "\nEnter 'quit' to finish. "
active = True

while active == True:
    topping_to_add = input(prompt)

    if topping_to_add != 'quit':
        print(f"You will add {topping_to_add} to your pizza")
        toppings.append(topping_to_add)
    else:
        active = False
        print("This is the list of toppings you want on your pizza:")
        for topping in toppings:
            print(f"\t{topping}")