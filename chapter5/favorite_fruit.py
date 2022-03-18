favorite_fruits = ['apples', 'orange', 'bananas']

fruits = ['grapes','tangerine','apples','bananas', 'strawberries', 'watermelon','orange']

for fruit in fruits:
    if fruit in favorite_fruits:
        print(f"You really love {fruit}")
    else:
        print(f"Are you sure you dislike {fruit}?")
