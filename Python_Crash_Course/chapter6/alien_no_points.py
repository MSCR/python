# Create a new alien without points element
alien_0 = {'color':'green', 'speed':'medium'}

# If you try to get an element that doesn't exist an keyError exception will be throw
# i.e.
# print(alien_0['points'])
# Traceback (most recent call last):
#    File "alien_no_points.py", line 2, in <module>
#        print(alien_0['points'])
# KeyError: 'points'

# Instead use method get()
points_value = alien_0.get('points','No point value assigned')
print(points_value)

# If second argument is not specified
points_value = alien_0.get('points')
print(points_value)

# If points is added
alien_0['points'] = 5
points_value = alien_0.get('points','No point value assigned')
print(points_value)