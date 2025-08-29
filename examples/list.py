# Basic usage of list in Python

# Creating a list
fruits = ["apple", "banana", "cherry"]

print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing elements
print(fruits[0])  # Output: apple

# Adding elements
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Removing elements
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# Iterating over a list
for fruit in fruits:
    print(fruit)

# List length
print(len(fruits))  # Output: 3
