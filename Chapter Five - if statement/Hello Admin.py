user_names= ["Sara" , "Nirvana" , "Kian", "Ali", "Bahar", "admin"]
for user_name in user_names:
    print(f"Welcome to this site {user_name.title()}")
    
    
print("-------------------------")

user_names= ["Sara" , "Nirvana" , "Kian", "Ali", "Bahar", "admin"]
for user_name in user_names:
    if user_name == "admin":
        print("Hello admin, would you like to see a status report")
    
    else:   
        print(f"Hello {user_name}, thank you for logging in again")
        






