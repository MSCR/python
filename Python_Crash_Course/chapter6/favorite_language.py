# Define a new dictionary
favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
# NOTE: As a good practice leave a coma in the last elemnt of the dictionary

language = favorite_language['sarah']
print(f"Sarah's favorite language is {language}\n")

# Let's loop thru the dictionary
print("\nLoop thru dictionary throught key-values")
for name,language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# Now, we will loop thru the dictionary throught the keys
print("\nLoop thru dictionary throught keys")
for name in favorite_language.keys():
    print(name.title())

# Looping thru keys is the default behaviour
print("\nAlternative way, loop thru dictionary throught keys")
for name in favorite_language:
    print(name.title())

# You can access the value during the looping
friends = ['phil','sarah']

print("\nAccess values when looping throught keys")
for name in favorite_language.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}")

print("")
if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll!!") 

# In order to loop thru a dictionary in order, you can use the sort function
print("")
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping thru dictionary throught values
print("\nLoop thru dictionary throught values")
print("The following languages was mentioned")
for language in favorite_language.values():
    print(language.title())

# Using sets you can avoid to print repeated values
print("\nThe following languages was mentioned")
for language in set(favorite_language.values()):
    print(language.title())

# Building a set from zero
languages = {'python', 'c', 'python', 'ruby'}
print("\nPrint a set")
print(languages)

# Let's create some nesting of lists and dictionaries
# Nest a dictionary in a dictionary

favorite_language = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}

for name,languages in favorite_language.items():
    if len(languages) > 1:
        print(f"\n{name.title()} favorite's lagunages are:")
    else:
        print(f"\n{name.title()} favorite's lagunages is:")
    for language in languages:
        print(f"{language.title()}")