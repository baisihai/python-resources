# Using dictionary comprehension to create a new dictionary with names that start with 'A'

names = [
    'Alice',
    'Bob',
    'Charlie',
    'Anna',
    'Aaron',
    'David',
    'Eve',
    'Alex'
]

filtered_names_dict = {name: len(name) for name in names if name.startswith('A')}
print("Filtered Names Dictionary:", filtered_names_dict)
# Output: Filtered Names Dictionary: {'Alice': 5, 'Anna': 4, 'Aaron': 5, 'Alex': 4}
