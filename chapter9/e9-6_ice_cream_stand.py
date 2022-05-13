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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'nuts', 'coconut', 'strawberry']

    def show_flavors(self):
        print(f"The Icecream stand {self.restaurant_name} offers the next flavors: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

my_stand = IceCreamStand("The polar bear", "icecream")
my_stand.show_flavors()