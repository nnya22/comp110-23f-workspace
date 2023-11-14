"""Practice with Dictionary Syntax"""

#Create a new dictionary
ice_cream: dict[str,int] = {"chocolate": 12, "vanilla": 8, "strawberry":5}
print("Create my dictionary:")
print(ice_cream)

#Adding a key value to the dictionary
ice_cream["mint"] = 3
print("Added mint to dictionary")
print(ice_cream)

#Removing a key value pair
ice_cream.pop("mint")
print("Removed mint:")
print(ice_cream)

#Accessing a value
print(f"There are {ice_cream['chocolate']} orders of chocolate")

#Updating a value
ice_cream["vanilla"] = 10
#ice_cream["vanilla"] += 2
print("After updating vanilla:")
print(ice_cream)

#Print the length
print(f"There are {len(ice_cream)} key-value pairs")

#Check if key in dictionary
print("Chocolate in dictionary?")
print("chocolate" in ice_cream)

#Using "in" in a conditional
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint.")

#Using "for" loops in dictionaries. "for" loops iterate over the keys by default. print out each flavor and number of order
for flavor in ice_cream:
    #print out each flavor and number of orders
    print(f"{flavor} has {ice_cream[flavor]} orders")