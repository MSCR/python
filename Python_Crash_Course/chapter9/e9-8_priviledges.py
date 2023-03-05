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

class Priviledges():

    def __init__(self):
        self.priviledges = ["can add post", "can delete post", "can be user"]

    def show_priviledges(self):
        print(f"User has the following priviledge: ")
        for priviledge in self.priviledges:
            print(f"- {priviledge}")

class Admin(User):

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.priviledges = Priviledges()

my_user = Admin('manuel', 'cortes', 32, 'queretaro')
my_user.priviledges.show_priviledges()