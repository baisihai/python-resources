# Python Dictionary Aggregation
# Combines two dictionaries by summing the values of common keys.
# Example: Aggregating two dictionaries representing an inventory and loot

inv = {
    'Sword': 1,
    'Portion': 3
}

loot = {
    'Sword': 1,
    'Portion': 2, 
    'Shield': 1
}

# Method 1: Using dictionary comprehension
print("Method 1: Using dictionary comprehension")
new_inv = {k: inv.get(k, 0) + loot.get(k, 0) for k in set(inv) | set(loot)}
print ("Updated Inventory:", new_inv,"\n")

# Method 2: Using the update() method
print("Method 2: Using the update() method")
print("Note: The update() method only combines the keys with the values from loot into inv.")
inv.update(loot)
print ("Updated Inventory:", inv)
