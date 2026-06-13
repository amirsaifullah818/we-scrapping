# List

foods = ["pizza", "burger", "burger", "soup", "soup"]

print(foods)


# Tuple
# You cannot add/remove/change any item in a tuple

armies = ["omar", "ahmed", "khalid", "khalid"]

print(armies)



# Set
# Does not allow any duplicates
# Does not maintain the order/serial
days = ["sat","sun","mon","tue","wed","thu","fri","fri"]

print(days)


emails = {
    "omar23@gmail.com"
    "ahmed42@gmail.com",
    "sakib11@gmail.com",
    "fatima77@yahoo.com"
}

print(emails)

# Now, We have a list of customers phone numbers
# But it have some duplicates
# Your task is to remove the duplicates
# and show the list without any duplicates


phone_numbers = ["123-555555", "987-6543210", "123-555555", "232-5555555", "232-5555555"]

phone_numbers_set = set(phone_numbers)

phone_numbers_list = list(phone_numbers_set)

print(phone_numbers_list)