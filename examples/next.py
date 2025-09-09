# The next() function in Python is a built-in function used to retrieve the next item from an iterator. 
# It is fundamental to manually controlling iteration over iterable objects like lists, tuples, strings, or custom iterators. 

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
