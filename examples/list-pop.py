inventory = [
    'Sword',
    'Armor',
    'Shield',
    'Gloves',
    'Torch',
    'Gem',
    'Boots'
]

print("Inventory:", inventory)
index=inventory.index('Shield')  # Finds index of 'Shield'
print(f"Index of 'Shield': {index}")
item=inventory.pop(index)  # Removes 'Shield' at index 2, and stores it in item
print(f"Removed item: {item}")
print("Updated Inventory:", inventory)

# Output:
# Inventory: ['Sword', 'Armor', 'Shield', 'Gloves', 'Torch', 'Gem', 'Boots']
# Index of 'Shield': 2
# Removed item: Shield  
# Updated Inventory: ['Sword', 'Armor', 'Gloves', 'Torch', 'Gem', 'Boots']
