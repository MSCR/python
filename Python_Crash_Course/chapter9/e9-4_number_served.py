class Restaurant:
    """Class restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """This function describes the restaurant"""
        print(f"This is the restauran {self.restaurant_name.title()} speceialize on {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """This function anounce the restaurant is open"""
        print(f"The restaurant {self.restaurant_name} is OPEN!!!!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("Il Tavolo", "french")

restaurant.number_served = 2
print(f"Number of customers served: {restaurant.number_served}")
restaurant.number_served = 5
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(3)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(1)
print(f"Number of customers served: {restaurant.number_served}")