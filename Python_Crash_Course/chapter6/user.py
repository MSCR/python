# Let's loop thru the values of a dictionary
# You can loop thru a dictionary through all of dictionary's
# key-values, throught its keys, or throught its values

# First let-s define this User dictionary
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

# Now we will loop thru key-values
for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# Additional notes
# key and value are variables that will contain the list
# items method will return. If you use k,n variables it
# will work as well

