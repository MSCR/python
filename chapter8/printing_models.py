def print_designs(unprinted_desings,completed_models):
    # Simulate printing each design, until none are left.
    # Move each design to completed_models after printing.
    while unprinted_desings:
        current_design = unprinted_desings.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_designs(completed_models):
    # Display all completed models.
    print("\nThe following models have been printed:")
    for completed_models in completed_models:
        print(completed_models)    


# Start with some designs that need to be printed.
unprinted_desings = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_designs(unprinted_desings[:], completed_models)

show_completed_designs(completed_models)

print("\nunprinted_desings")
print(unprinted_desings)
print("completed_models")
print(completed_models)