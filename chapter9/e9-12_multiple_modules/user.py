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
