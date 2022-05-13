class Restaurant:
    """Class restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """This function describes the restaurant"""
        print(f"This is the restauran {self.restaurant_name.title()} speceialize on {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """This function anounce the restaurant is open"""
        print(f"The restaurant {self.restaurant_name} is OPEN!!!!")

my_restaurant = Restaurant("El amigo", "french")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()