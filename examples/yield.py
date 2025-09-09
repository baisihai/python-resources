# Example of a simple generator function using yield
# The yield statement allows a function to return a value and later resume to continue from where it left off.

def simple_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# Create a generator object
gen = simple_generator()

# Iterate through the generator
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
for value in gen:
    print(value)  # Output: 3, 4 and 5 (the loop continues from where next(gen) left off)
