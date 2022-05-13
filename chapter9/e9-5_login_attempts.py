class User:
    """This class define the User object"""

    def __init__(self, first_name, last_name, age, location):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first.title()} {self.last.title()} is {self.age} years old and "
            f"lives in {self.location.title()}")

    def greet_user(self):
        print(f"Hello {self.first.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts increased to {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts has been reset to {self.login_attempts}")

my_user = User('Manuel', 'Cortes', 32, 'Queretaro')
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.reset_login_attempts()
my_user.increment_login_attempts()
