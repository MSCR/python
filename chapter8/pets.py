# This function has 2 parameters
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# Passing argumens by order
describe_pet("kirara","cat")
# Passing arguments by Keyboard
describe_pet(pet_name="akane", animal_type="guinea pig")
# Using default value
describe_pet('charly')