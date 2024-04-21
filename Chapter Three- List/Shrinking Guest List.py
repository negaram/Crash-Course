guests=["Enistin", "Marie Curie", "Ilan Mask"]
guests.insert(0 , "Fee Fee Lee")
#print(guests)
guests.insert(2 , "Andrew NG")
#print(guests)
guests.append("Mahmod Hesabi")
print(guests)

pop_guests= guests.pop()
print(f" Sorry dear {pop_guests}, I have a problem. I will invite you soon")
pop_guests1= guests.pop()
print(f" Sorry dear {pop_guests1}, I have a problem. I will invite you soon")
pop_guests2= guests.pop()
print(f" Sorry dear {pop_guests2}, I have a problem. I will invite you soon")
pop_guests3= guests.pop()
print(f" Sorry dear {pop_guests3}, I have a problem. I will invite you soon")
print(guests)

del guests[0]
print(guests)
del guests[0]
print(guests)