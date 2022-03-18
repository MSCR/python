# List with current users
current_users = ['mscortes','admin','cacortes','macortes','mgcortes','damartinez','john']

# List with new users
new_users = ['dmartinez','esolorio','mscortes','rmartinez', 'John', 'ADMIN']

for user in new_users:
    if user.lower() in current_users:
        print("Please, enter a new user")
    else:
        current_users.append(user)
        print(f"User {user} added to the list")

print("\nPrint user list\n")

for user in current_users:
    print(user)