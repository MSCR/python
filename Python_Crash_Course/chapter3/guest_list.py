# Create first list of guests
guests = ['Juan','Aaron','Celis']

# Print the list and send the invitations
print(f"List of guests:\n\t{guests[0].title()}\n\t{guests[1].title()}\n\t{guests[2].title()}\n")

print(f"List lenght:{len(guests)}\n\n")

print(f"Hi {guests[0].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"Hi {guests[1].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"Hi {guests[2].title()} you are invited to a dinner at my house at 8:00 PM\n")

# Guest is not able to assist
guest_no = 1

print(f"Sorry, {guests.pop(guest_no).title()} will not attend the dinner\n")

print(f"List lenght:{len(guests)}\n\n")

# Add new guest
guests.insert(guest_no,'Alexis')

print(f"List of guests:\n\t{guests[0].title()}\n\t{guests[1].title()}\n\t{guests[2].title()}\n")

print(f"Hi {guests[0].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"Hi {guests[1].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"Hi {guests[2].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"List lenght:{len(guests)}\n\n")

print("A bigger table was found, we will add more guests")

# Add more guest to the table
guests.insert(0, 'Martin')

guests.insert(-2, 'Jorge')

guests.append('Luis')

print(f"List of guests:\n\t{guests[0].title()}\n\t{guests[1].title()}\n\t{guests[2].title()}\n\t{guests[3].title()}\n\t{guests[4].title()}\n\t{guests[5].title()}\n")

print(f"Hi {guests[0].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"Hi {guests[1].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"Hi {guests[2].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"Hi {guests[3].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"Hi {guests[4].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"Hi {guests[5].title()} you are invited to a dinner at my house at 8:00 PM\n")

print(f"List lenght:{len(guests)}\n\n")

# New table will not arrive on time
print("Sorry, new table will not arrive on time\n")

# Remove guest, only two can be invited
print(f"Sorry {guests.pop().title()},I cannot invite you to the dinner")
print(f"Sorry {guests.pop().title()},I cannot invite you to the dinner")
print(f"Sorry {guests.pop().title()},I cannot invite you to the dinner")
print(f"Sorry {guests.pop().title()},I cannot invite you to the dinner")

print(f"Hi {guests[0].title()}, you are still invited to the dinner")
print(f"Hi {guests[1].title()}, you are still invited to the dinner")

print(f"List lenght:{len(guests)}\n\n")

del guests[1]
del guests[0]

print(guests)

print(f"List lenght:{len(guests)}\n\n")