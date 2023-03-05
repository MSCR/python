class User:
    """This class define the User object"""

    def __init__(self, first_name, last_name, age, location):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"\n{self.first.title()} {self.last.title()} is {self.age} years old and "
            f"lives in {self.location.title()}")

    def greet_user(self):
        print(f"Hello {self.first.title()}")


my_user = User('Manuel', 'Cortes', 32, 'Queretaro')
my_wife = User('Dinorha', 'Martinez', 28, 'Queretaro')
my_sister = User('Maria', 'Cortes', 20, 'Guadalajara')
my_brother = User('Carlos', 'Cortes', 25, 'Pajacuaran')

my_user.describe_user()
my_user.greet_user()

my_wife.describe_user()
my_wife.greet_user()

my_sister.describe_user()
my_sister.greet_user()

my_brother.describe_user()
my_brother.greet_user()