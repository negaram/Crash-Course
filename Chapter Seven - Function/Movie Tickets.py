prompt ="Enter your age: "

while True:
    age =int(input(prompt))
    if age < 3:
      print("your ticket is free")
    elif 3<= age < 12:
      print ("your ticket is 10$")
    elif age >= 12:
      print("your ticket is 15$")
         