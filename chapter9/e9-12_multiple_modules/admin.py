from user import User

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