# Using list comprehension to create a new list with names that start with 'A'

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

filtered_names_list = [name for name in names if name.startswith('A')]
print("Filtered Names:", filtered_names_list)
