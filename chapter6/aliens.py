# Let's create some nesting of lists and dictionaries

# Nest a dictionary in a list
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Now lets create a list of 30 aliens automatically

# Make empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

# Let's modify some aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] =10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...\n")

# Show how many aliens have been created
print(f"Total number of alies: {len(aliens)}")

# Access an specific element
print(f"Accessing color of alien 1: {aliens[1]['color']}")