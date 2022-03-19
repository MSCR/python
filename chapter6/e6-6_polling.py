# Define a new dictionary
person = ['aaon','cesar','manuel','sarah','alice']

favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

for name in person:
    if name in favorite_language:
        print("Thanks for taking the poll.")
    else:
        print(f"{name.title()} please take the poll.")