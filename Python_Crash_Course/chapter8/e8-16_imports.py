from printing_functions import *

# Start with some designs that need to be printed.
unprinted_desings = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_designs(unprinted_desings[:], completed_models)

show_completed_designs(completed_models)

print("\nunprinted_desings")
print(unprinted_desings)
print("completed_models")
print(completed_models)