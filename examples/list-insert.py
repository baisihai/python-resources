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
item = 'Potion'
inventory.insert(1, item)  # Inserts 'Shield' at index 1
print(f"Inserted item: {item}")
print("Updated Inventory:", inventory)

# Output:
# Inventory: ['Sword', 'Armor', 'Shield', 'Gloves', 'Torch', 'Gem', 'Boots']
# Inserted item: Potion
# Updated Inventory: ['Sword', 'Potion', 'Armor', 'Shield', 'Gloves', 'Torch', 'Gem', 'Boots']
