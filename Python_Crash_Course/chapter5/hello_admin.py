# Empty list
#users = []

# List with users
users = ['mscortes','admin','cacortes','macortes','mgcortes','damartinez']

# Verify list is not empty
if users:
    # Print greetings to the users
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again")
else:
    print("We need to find some users!")