# Python Dictionary Aggregation
# Combines two dictionaries by summing the values of common keys.
# Example: Aggregating two dictionaries representing an inventory and loot

inventory = {
    'Sword': 1,
    'Potion': 3
}

loot = {
    'Sword': 1,
    'Potion': 2, 
    'Shield': 1
}

# Method 1: Using dictionary comprehension
print("Method 1: Using dictionary comprehension")
new_inventory = {k: inventory.get(k, 0) + loot.get(k, 0) for k in set(inventory) | set(loot)}
print ("Updated Inventory:", new_inventory,"\n")

# Method 2: Using the update() method
print("Method 2: Using the update() method")
print("Note: The update() method only combines the keys with the values from loot into inventory.")
inventory.update(loot)
print ("Updated Inventory:", inventory)
