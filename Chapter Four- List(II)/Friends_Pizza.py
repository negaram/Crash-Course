pizzas = ["Pepperoni", "Chicken", "Vegtable"]
friend_pizzas= pizzas[:]
pizzas.append("Sausage")
friend_pizzas.append("New York")
print(f"My favorite pizzas are:{pizzas}\n")
for pizza in pizzas:
    print(pizza)
print(f"\nMy friends'favorite pizzas are:{friend_pizzas}")
for pizzaa in friend_pizzas:
    print(pizzaa)