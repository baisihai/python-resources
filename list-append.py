inventory = [
    'Sword',
    'Armor',
    'Boots'
]

chest = [
    'Map',
    'Potion', 
    'Shield'
]

# Method: Using the append() method in a loop
for item in chest:
    inventory.append(item)
print("Updated Inventory:", inventory)
