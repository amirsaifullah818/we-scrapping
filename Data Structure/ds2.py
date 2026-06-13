# Topic: Dictionary


product = {
    "name": "T-shirt",
    "color": "Gray",
    "price": 19.99,
    "sizes":["S","M","L","XL"],
    "stock": 100
}




print(product)

print(product["name"])

print(product["color"])


# Change any value
product["price"] = 24.99


print(product)


product["stock"] = 80

print(product)



# some functions of dictionary

print( product.keys()  )




# find all the values
print( product.values()  )


# find all the items

print ( product.items()  )


# access the dictionary

# find the price of the product

print( product.get("price") )

# find the size of the product

sizes = product.get("sizes")

print(sizes)


print(product.items())






# loop through the dictionary

for key,value in product.items():
    print(key)



# another loop
for key,value in product.items():
    print(value)


# another loop
for key,value in product.items():
    print(key, "is", value)








PC = {
    "name": "Lenovo",
    "color": "black",
    "RAM": "8GB",
    "SSD": "256GB"
}





for key,value in PC.items():
    print("The",key,"is",value)



Phone = {
    "brand": "Apple",
    "color": "Silver",
    "size": "Mini",
    "model": "Iphone"
}

for key,value in Phone.items():
    print("The",key,"is",value)