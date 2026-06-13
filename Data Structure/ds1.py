
# Data structures of Python
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary



# List: Storing many items together


friends = ["Omar","Sulaiman","Noman","Hasan"]

print(friends)

# access any item using position/index number

print(friends[0])

print(friends[1])


# add any item
friends.append("Ali")

print(friends)


# remove any item
friends.remove("Hasan")

print(friends)


# change any item
friends[0]= "Ahmed"

print(friends)





# Dictionary: Storing detailed information about something

person = {
    "name": "Abdur Rahman",
    "age": 25,
    "city": "Dhaka",
    "fav_foods": ["biryani","pizza","kacchi"],
    "blood_group": "O+"
}




print(person)

# acces to any item using key
print(person["name"])
print(person["blood_group"])
print(person["fav_foods"])
print(person["city"])



sodas = ["sprite", "coca-cola", "fanta", "pepsi"]

print(sodas)

print(sodas[1])

sodas.append("Dr Pepper")

print(sodas)

sodas.remove("fanta")

print(sodas)

sodas[0] = "mountain dew"

print(sodas)

drink_info = {
    "brand": "Coca-Cola",
    "type": "Soft Drink",
    "flavors": ["classic cola", "cherry cola", "vanilla cola"],
    "country": "USA",
    "is_cold": "yes"
}

print(drink_info)

print(drink_info["type"])
print(drink_info["flavors"])
print(drink_info["country"])