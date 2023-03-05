def get_formatted_name(first, last, middle=""):
    """Return a full name, neatly formated"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

musician = get_formatted_name("jimmy","hendrix")
print(musician)

musician = get_formatted_name("jhon","hooker","lee")
print(musician)

# This is an infinite loop
while True:
    print("\nPlease tell me your name:" )
    print("Press 'q' at any time to quit")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formated_name = get_formatted_name(f_name,l_name)
    print(f"\nHello {formated_name}!!")