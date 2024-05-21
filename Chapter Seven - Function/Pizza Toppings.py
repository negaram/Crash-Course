prompt = "\nPlease enter the name of a pizza you want to eat:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    pizza = input(prompt)
    if pizza == 'quit':
        break
    else:
        print(f"I'd love to eat  {pizza.title()}!")