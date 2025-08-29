# Basic usage of dictionary in Python

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: Alice
print(person.get("name"))  # Output: Alice; This method is safer. If a key doesn't exist, it returns None instead of raising an error.
print(person.get("name", "Not Found"))  # Output: Alice; If the key doesn't exist, it returns "Not Found".
print("")

# Adding a new key-value pair
person["email"] = "alice@example.com"

# Updating a value
person["age"] = 31

# Removing a key-value pair
del person["city"]

# Iterating over keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "email" in person:
    print("Email is present.")

# Getting all keys and values
keys = list(person.keys())
values = list(person.values())
print("Keys:", keys)
print("Values:", values)

