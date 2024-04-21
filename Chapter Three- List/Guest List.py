guests=["Enistin", "Marie Curie", "Ilan Mask"]
print(f" Hello Sweetie {guests[0]} come to our party on Wednesday")
print(f" Hello Sweetie {guests[1]} come to our party on Wednesday")
print(f" Hello Sweetie {guests[2]} come to our party on Wednesday")
pop_invite =  guests.pop(0)
print(f"{pop_invite} can't come tonight")
print(guests)
guests.insert(0, "Fee Fee Lee")
print(f" Hello Sweetie {pop_invite} can't come tonight. instead of {pop_invite} , I invite {guests[0]}")