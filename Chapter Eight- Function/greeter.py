def greet_user():
 """Display a simple greeting."""
 print("Hello!")
greet_user()

print("-----------------------------------")


def greet_user(username):
 """Display a simple greeting."""
 print(f"Hello, {username.title()}!")
greet_user('jesse')
