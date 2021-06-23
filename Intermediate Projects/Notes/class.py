# A class is a blueprint for a project
# A constructor is part of the blueprint which specifices what happens.
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # Self is the actual object being initialized aka the USER

    # Capital letters always. Term is known as PascalCase
    def add_followers(self, user):
        self.following += 1
        user.followers += 1

    # なんで？
    # All the code that would be in the class will be indented
    # The pass simply removes the error when indentation intervenes
user_1 = User("001", "angela")
print(user_1.username)
user_2 = User("002", "markoson")
print(user_2.id)

user_1.add_followers(user_2)
user_1.add_followers(user_2)
user_1.add_followers(user_2)
print(user_1.following)

# How can we make this simplier?
