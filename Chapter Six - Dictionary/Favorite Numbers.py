favorite_number={
    "Negar":22,
    "Bahar": 7,
    "Kian": 19,
    "Mandana": 6,
    "Hasti":11,
}
print(f" this is our team and their favorite color:")
for people in favorite_number:
    print(f" {people} favorite number is {favorite_number[people]} ")
    
    
print("-------------------------")


favorite_number={
    "Negar":22,
    "Bahar": 7,
    "Kian": 19,
    "Mandana": 6,
    "Hasti":11,
}
print(f" this is our team and their favorite color:")
for people,value in favorite_number.items():
    print(f" {people} favorite number is {value} ")
    
print("-------------------------------------")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
for name, language in favorite_languages.items():
 print(f"{name.title()}'s favorite language is {language.title()}.")
    