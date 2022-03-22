prompt = "\nHi, welcome to Multicinema,"
prompt += "\nHow old are you to check the cost of the ticket? "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free")
        elif age >= 3 and age <= 12:
            print("Your ticket cost $10")
        elif age > 12:
            print("Your ticket cost $15")