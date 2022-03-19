# A dictionary is build using a set of key:value
# The key is always a string
# The value can be any type of data, i.e. string, int, list, dictionary. It could contain also classes

# A dictionary can be created with pre-defined data or empty and add new elements

# i.e.
# Create a dictionary with pre-defined data
alien_0 = {'color':'green','points':5}

# Create an empty Dictionary
alien_0 = {}

# i.e.
# Add new elements to Dictionary
alien_0['color'] = 'green'
# Add a second element to Dictionary
alien_0['points'] = 5
# NOTE: When printing the elements of a dictionary in a loop, they will be printed in the
# same order as they was added to the dictionary

# You can print access the values of the dictionary and print it
# i.e.
# Print all elements of the dictionary
print(alien_0)
# Print specific element
print(f"The color of the alien is {alien_0['color']}")
print(f"The points of the alien is {alien_0['points']}")

# In order to add modify an element, it works the same as adding a new element
# i.e.
# Set color element
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}")
# Modify value of color element
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

# i.e.
# Modifying dictionary values
alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Let's check how to remove an element from the dictionary
alien_0 = {'color':'green', 'points':5, 'x_position':0, 'y_position':25, 'speed':'medium'}
print(alien_0)

# Using the del() function we can remove an element from the dictionary
del(alien_0['points'])
print(alien_0)