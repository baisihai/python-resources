'''
The zip() function in Python is a built-in utility that aggregates elements from multiple iterables into a single iterable of tuples. Each tuple contains corresponding elements from the input iterables.

How it works:
zip() takes one or more iterables (e.g., lists, tuples, strings) as arguments.
It returns an iterator that yields tuples.
Each tuple contains the element at the same index from each of the input iterables.
The zip() function stops when the shortest input iterable is exhausted, discarding any remaining elements from longer iterables.

Common Use Cases:
1) Parallel Iteration:
Iterating over multiple lists or sequences simultaneously, pairing up related elements.

2) Dictionary Creation:
Combining two lists (one for keys, one for values) to create a dictionary using dict(zip(keys, values)).

3) Unzipping:
Using the * (unpacking) operator with zip() to reverse the process and separate zipped elements back into individual iterables.
'''

from itertools import repeat
from itertools import cycle
from itertools import islice
from itertools import tee
from itertools import chain
from itertools import zip_longest
from itertools import starmap
from itertools import compress
from itertools import filterfalse
from itertools import accumulate
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import groupby
from itertools import islice
from itertools import zip_longest

# Example 1: Basic Usage
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped = zip(names, ages)
print("Zipped:", list(zipped))
# Output: Zipped: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]



# Example 2: Different Lengths
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30]
zipped = zip(names, ages)
print("")   # Just to add a blank line for better readability of output
print("Zipped with different lengths:", list(zipped))
# Output: Zipped with different lengths: [('Alice', 25), ('Bob', 30)]



# Example 3: Creating a Dictionary
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
zipped_dict = dict(zip(keys, values))
print("")   # Just to add a blank line for better readability of output
print("Zipped Dictionary:", zipped_dict)
# Output: Zipped Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}



# Example 4: Unzipping
zipped = [('Alice', 25), ('Bob', 30), ('Charlie',35)]
names, ages = zip(*zipped)
print("")   # Just to add a blank line for better readability of output
print("Unzipped Names:", names)
print("Unzipped Ages:", ages)
# Output:
# Unzipped Names: ('Alice', 'Bob', 'Charlie')
# Unzipped Ages: (25, 30, 35)



# Example 5: Using with Different Iterables
list1 = [1, 2, 3]
tuple1 = ('a', 'b', 'c')
string1 = "XYZ"
zipped = zip(list1, tuple1, string1)
print("")   # Just to add a blank line for better readability of output
print("Zipped with different iterables:", list(zipped))
# Output: Zipped with different iterables: [(1, 'a', 'X'), (2, 'b', 'Y'), (3, 'c', 'Z')]



# Example 6: Iterating Over Zipped Object
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
print("")   # Just to add a blank line for better readability of output
print("Iterating Over Zipped Object")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
# Output:
# Alice is 25 years old.
# Bob is 30 years old.
# Charlie is 35 years old.



# Example 7: Zipping with List Comprehension
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped_list = [f"{name} is {age} years old." for name, age in zip(names, ages)]
print("")   # Just to add a blank line for better readability of output
print("Zipped List with Comprehension:", zipped_list)
# Output: Zipped List with Comprehension: ['Alice is 25 years old.', 'Bob is 30 years old.', 'Charlie is 35 years old.']



# Example 8: Zipping with More Than Two Iterables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]
zipped = zip(list1, list2, list3)
print("")   # Just to add a blank line for better readability of output
print("Zipped with three iterables:", list(zipped))
# Output: Zipped with three iterables: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]



# Example 9: Zipping with Empty Iterables
list1 = [1, 2, 3]
list2 = []
zipped = zip(list1, list2)
print("")   # Just to add a blank line for better readability of output
print("Zipped with an empty iterable:", list(zipped))
# Output: Zipped with an empty iterable: []



# Example 10: Zipping with Generators
def gen1():
    for i in range(3):
        yield i
def gen2():
    for char in 'abc':
        yield char
zipped = zip(gen1(), gen2())
print("")   # Just to add a blank line for better readability of output
print("Zipped with generators:", list(zipped))
# Output: Zipped with generators: [(0, 'a'), (1, 'b'), (2, 'c')]



# Example 11: Zipping with Different Data Types
list1 = [1, 2, 3]
list2 = ['one', 'two', 'three']
zipped = zip(list1, list2)
print("")   # Just to add a blank line for better readability of output
print("Zipped with different data types:", list(zipped))
# Output: Zipped with different data types: [(1, 'one'), (2, 'two'), (3, 'three')]



# Example 12: Zipping with Nested Iterables
list1 = [[1, 2], [3, 4], [5, 6]]
list2 = [['a', 'b'], ['c', 'd'], ['e', 'f']]
zipped = zip(list1, list2)
print("")   # Just to add a blank line for better readability of output
print("Zipped with nested iterables:", list(zipped))
# Output: Zipped with nested iterables: [([1, 2], ['a', 'b']), ([3, 4], ['c', 'd']), ([5, 6], ['e', 'f'])]



# Example 13: Zipping with Different Lengths and Filling Values
from itertools import zip_longest
list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = zip_longest(list1, list2, fillvalue='N/A')
print("")   # Just to add a blank line for better readability of output
print("Zipped with different lengths and fill values:", list(zipped))
# Output: Zipped with different lengths and fill values: [(1, 'a'), (2, 'b'), (3, 'N/A')]



# Example 14: Zipping with Custom Objects
class Person:
    def __init__(self, name):
        self.name = name
class Age:
    def __init__(self, age):
        self.age = age
people = [Person('Alice'), Person('Bob'), Person('Charlie')]
ages = [Age(25), Age(30), Age(35)]
zipped = zip(people, ages)
print("")   # Just to add a blank line for better readability of output
print("Zipping with Custom Objects:")
for person, age in zipped:
    print(f"{person.name} is {age.age} years old.")
# Output:
# Alice is 25 years old.
# Bob is 30 years old.
# Charlie is 35 years old.



# Example 15: Zipping with List of Different Lengths
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
zipped = zip(list1, list2)
print("")   # Just to add a blank line for better readability of output
print("Zipped with lists of different lengths:", list(zipped))
# Output: Zipped with lists of different lengths: [(1, 'a'), (2, 'b')]



# Example 16: Zipping with List Comprehension and Condition
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
zipped = [f"{num}-{char}" for num, char in zip(list1, list2) if num % 2 == 0]
print("")   # Just to add a blank line for better readability of output
print("Zipped with comprehension and condition:", zipped)
# Output: Zipped with comprehension and condition: ['2-b', '4-d']



# Example 17: Zipping with Multiple Iterables of Different Types
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
tuple1 = (True, False, True)
zipped = zip(list1, list2, tuple1)
print("")   # Just to add a blank line for better readability of output
print("Zipped with multiple iterables of different types:", list(zipped))
# Output: Zipped with multiple iterables of different types: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]



# Example 18: Zipping with List of Tuples
list1 = [(1, 'a'), (2, 'b'), (3, 'c')]
list2 = [(True, 10), (False, 20), (True,
30)]
zipped = zip(list1, list2)
print("")   # Just to add a blank line for better readability of output
print("Zipped with list of tuples:", list(zipped))
# Output: Zipped with list of tuples: [((1, 'a'), (True, 10)), ((2, 'b'), (False, 20)), ((3, 'c'), (True, 30))]



# Example 19: Zipping with List of Different Lengths and Ignoring Extra Elements
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print("")   # Just to add a blank line for better readability of output
print("Zipped with different lengths, ignoring extras:", list(zipped))
# Output: Zipped with different lengths, ignoring extras: [(1, 'a'), (2, 'b'), (3, 'c')]



# Example 20: Zipping with List of Different Lengths and Filling Missing Values
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=None)
print("")   # Just to add a blank line for better readability of output
print("Zipped with different lengths, filling missing values:", list(zipped))
# Output: Zipped with different lengths, filling missing values: [(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]



# Example 21: Zipping with List of Different Lengths and Custom Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue='N/A')
print("")   # Just to add a blank line for better readability of output
print("Zipped with different lengths, custom fill value:", list(zipped))
# Output: Zipped with different lengths, custom fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'N/A'), (5, 'N/A')]



# Example 22: Zipping with List of Different Lengths and Using itertools.cycle
from itertools import cycle
list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = zip(list1, cycle(list2))
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.cycle:", list(zipped))
# Output: Zipped with itertools.cycle: [(1, 'a'), (2, 'b'), (3, 'a')]



# Example 23: Zipping with List of Different Lengths and Using itertools.islice
from itertools import islice
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip(list1, islice(cycle(list2), len(list1)))
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.islice:", list(zipped))
# Output: Zipped with itertools.islice: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'a'), (5, 'b')]



# Example 24: Zipping with List of Different Lengths and Using itertools.tee
from itertools import tee
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list2_1, list2_2 = tee(cycle(list2))
zipped = zip(list1, list2_1)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.tee:", list(zipped))
# Output: Zipped with itertools.tee: [(1, 'a'), (2, (3, 'b'), (4, 'c'), (5, 'a')]



# Example 25: Zipping with List of Different Lengths and Using itertools.chain
from itertools import chain
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip(list1, chain(list2, repeat('N/A')))
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.chain:", list(zipped))
# Output: Zipped with itertools.chain: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'N/A'), (5, 'N/A')]



# Example 26: Zipping with List of Different Lengths and Using itertools.starmap
from itertools import starmap
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip(list1, cycle(list2))
zipped_starmap = starmap(lambda x, y: (x, y), zipped)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.starmap:", list(zipped_starmap))
# Output: Zipped with itertools.starmap: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'a'), (5, 'b')]



# Example 27: Zipping with List of Different Lengths and Using itertools.compress
from itertools import compress
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
selectors = [True, False, True, False, True]
zipped = zip(list1, list2)
zipped_compress = compress(zipped, selectors)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.compress:", list(zipped_compress))
# Output: Zipped with itertools.compress: [(1, 'a'), (3, 'c'), (5, None)]



# Example 28: Zipping with List of Different Lengths and Using itertools.filterfalse
from itertools import filterfalse
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
zipped_filterfalse = filterfalse(lambda x: x[0] % 2 == 0, zipped)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.filterfalse:", list(zipped_filterfalse))
# Output: Zipped with itertools.filterfalse: [(1, 'a'), (3, 'c'), (5, None)]



# Example 29: Zipping with List of Different Lengths and Using itertools.accumulate
from itertools import accumulate
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
zipped_accumulate = accumulate(zipped, lambda x, y: (x[0] + y[0], y[1]))
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.accumulate:", list(zipped_accumulate))
# Output: Zipped with itertools.accumulate: [(1, 'a'), (3, 'b'), (6, 'c')]



# Example 30: Zipping with List of Different Lengths and Using itertools.product
from itertools import product
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = product(list1, list2)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.product:", list(zipped))
# Output: Zipped with itertools.product: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]



# Example 31: Zipping with List of Different Lengths and Using itertools.permutations
from itertools import permutations
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = permutations(zip(list1, list2))
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.permutations:", list(zipped))
# Output: Zipped with itertools.permutations: [((1, 'a'), (2, 'b'), (3, 'c')), ((1, 'a'), (3, 'c'), (2, 'b')), ((2, 'b'), (1, 'a'), (3, 'c')), ((2, 'b'), (3, 'c'), (1, 'a')), ((3, 'c'), (1, 'a'), (2, 'b')), ((3, 'c'), (2, 'b'), (1, 'a'))]



# Example 32: Zipping with List of Different Lengths and Using itertools.combinations
from itertools import combinations
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = combinations(zip(list1, list2), 2)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.combinations:", list(zipped))
# Output: Zipped with itertools.combinations: [((1, 'a'), (2, 'b')), ((1, 'a'), (3, 'c')), ((2, 'b'), (3, 'c'))]



# Example 33: Zipping with List of Different Lengths and Using itertools.combinations_with_replacement
from itertools import combinations_with_replacement
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = combinations_with_replacement(zip(list1, list2), 2)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.combinations_with_replacement:", list(zipped))
# Output: Zipped with itertools.combinations_with_replacement: [((1, 'a'), (1, 'a')), ((1, 'a'), (2, 'b')), ((1, 'a'), (3, 'c')), ((2, 'b'), (2, 'b')), ((2, 'b'), (3, 'c')), ((3, 'c'), (3, 'c'))]



# Example 34: Zipping with List of Different Lengths and Using itertools.groupby
from itertools import groupby
list1 = [1, 2, 2, 3, 3, 3]
list2 = ['a', 'b', 'b', 'c', 'c', 'c']
zipped = zip(list1, list2)
zipped_groupby = groupby(zipped, key=lambda x: x[0])
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.groupby:")
for key, group in zipped_groupby:
    print(f"Key: {key}, Group: {list(group)}")
# Output:
# Zipped with itertools.groupby:
# Key: 1, Group: [(1, 'a')]
# Key: 2, Group: [(2, 'b'), (2, 'b')]
# Key: 3, Group: [(3, 'c'), (3, 'c'), (3, 'c')]



# Example 35: Zipping with List of Different Lengths and Using itertools.islice with a Step
from itertools import islice
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
zipped_islice = islice(zipped, 0, None, 2)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.islice and step:", list(zipped_islice))
# Output: Zipped with itertools.islice and step: [(1, 'a'), (3, 'c')]



# Example 36: Zipping with List of Different Lengths and Using itertools.zip_longest with a Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue='N/A')
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'N/A'), (5, 'N/A')]



# Example 37: Zipping with List of Different Lengths and Using itertools.zip_longest with None as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=None)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and None as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and None as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]



# Example 38: Zipping with List of Different Lengths and Using itertools.zip_longest with a Custom Object as Fill Value
class CustomFill:
    def __repr__(self):
        return "<CustomFill>"
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=CustomFill())
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and custom object as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and custom object as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, <CustomFill>), (5, <CustomFill>)]



# Example 39: Zipping with List of Different Lengths and Using itertools.zip_longest with a Mutable Object as Fill Value
class MutableFill:
    def __init__(self):
        self.value = "Mutable"
    def __repr__(self):
        return f"<MutableFill: {self.value}>"
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=MutableFill())
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and mutable object as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and mutable object as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, <MutableFill: Mutable>), (5, <MutableFill: Mutable>)]



# Example 40: Zipping with List of Different Lengths and Using itertools.zip_longest with a Function as Fill Value
def fill_function():
    return "FunctionFill"
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=fill_function())
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and function as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and function as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'FunctionFill'), (5, 'FunctionFill')]



# Example 41: Zipping with List of Different Lengths and Using itertools.zip_longest with a Lambda as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=(lambda: "LambdaFill")())
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and lambda as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and lambda as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'LambdaFill'), (5, 'LambdaFill')]



# Example 42: Zipping with List of Different Lengths and Using itertools.zip_longest with a List as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=['ListFill'])
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and list as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and list as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, ['ListFill']), (5, ['ListFill'])]



# Example 43: Zipping with List of Different Lengths and Using itertools.zip_longest with a Dictionary as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue={'key': 'DictFill'})
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and dictionary as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and dictionary as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, {'key': 'DictFill'}), (5, {'key': 'DictFill'})]



# Example 44: Zipping with List of Different Lengths and Using itertools.zip_longest with a Set as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue={'SetFill'})
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and set as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and set as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, {'SetFill'}), (5, {'SetFill'})]



# Example 45: Zipping with List of Different Lengths and Using itertools.zip_longest with a Tuple as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=('TupleFill',))
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and tuple as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and tuple as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, ('TupleFill',)), (5, ('TupleFill',))]



# Example 46: Zipping with List of Different Lengths and Using itertools.zip_longest with a Number as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=0)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and number as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and number as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 0), (5, 0)]



# Example 47: Zipping with List of Different Lengths and Using itertools.zip_longest with a Boolean as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=False)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and boolean as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and boolean as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, False), (5, False)]



# Example 48: Zipping with List of Different Lengths and Using itertools.zip_longest with an Empty String as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue='')
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and empty string as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and empty string as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, ''), (5, '')]



# Example 49: Zipping with List of Different Lengths and Using itertools.zip_longest with a Space as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=' ')
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and space as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and space as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, ' '), (5, ' ')]



# Example 50: Zipping with List of Different Lengths and Using itertools.zip_longest with a Newline as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue='\n')
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and newline as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and newline as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, '\n'), (5, '\n')]



# Example 51: Zipping with List of Different Lengths and Using itertools.zip_longest with a Tab as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue='\t')
print("*****")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and tab as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and tab as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, '\t'), (5, '\t')]



# Example 52: Zipping with List of Different Lengths and Using itertools.zip_longest with a Custom String as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue='CustomFill')
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and custom string as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and custom string as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'CustomFill'), (5, 'CustomFill')]



# Example 53: Zipping with List of Different Lengths and Using itertools.zip_longest with a Custom Number as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=999)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and custom number as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and custom number as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 999), (5, 999)]



# Example 54: Zipping with List of Different Lengths and Using itertools.zip_longest with a Custom Boolean as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=True)
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and custom boolean as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and custom boolean as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, True), (5, True)]



# Example 55: Zipping with List of Different Lengths and Using itertools.zip_longest with a Custom List as Fill Value
from itertools import zip_longest
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = zip_longest(list1, list2, fillvalue=['Custom', 'List'])
print("")   # Just to add a blank line for better readability of output
print("Zipped with itertools.zip_longest and custom list as fill value:", list(zipped))
# Output: Zipped with itertools.zip_longest and custom list as fill value: [(1, 'a'), (2, 'b'), (3, 'c'), (4, ['Custom', 'List']), (5, ['Custom', 'List'])]



# Example 56: Matching Elements from Two Lists, and inform where they differ
# The zip() function pairs elements from both lists, and the list comprehension checks for differences.
#   The enumerate() function provides the index of each pair, which is collected in the differences list.
# This approach is efficient and concise for comparing two lists element-wise.
# It can be particularly useful in data validation and testing scenarios.
# The output is a list of indices where the elements in the two lists do not match.
#
# This method can be adapted for lists of different lengths by using itertools.zip_longest if needed.
# This example demonstrates a practical use case of the zip() function in Python for comparing two lists.
# It highlights how to identify and report differences effectively.
# The final output provides a clear indication of where the two lists diverge.
#
# This technique can be extended to more complex data structures as well.
# It showcases the versatility of the zip() function in handling various data comparison tasks.
# The example is straightforward and easy to understand, making it accessible for beginners.
# It also serves as a foundation for more advanced data processing techniques.
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 0, 4, 0]
zipped = zip(list1, list2)
differences = [i for i, (a, b) in enumerate(zipped) if a != b]
print("")   # Just to add a blank line for better readability of output
print("Indices where elements differ:")
print("List1:", list1)
print("List2:", list2)
print("Different at index:", differences)
# Output: Indices where elements differ: [2, 4]
#   Explanation: The elements at index 2 and 4 are different in the two lists.
#   At index 2, list1 has 3 and list2 has 0.
#  At index 4, list1 has 5 and list2 has 0.
#  All other elements are the same in both lists.
# This is useful for quickly identifying discrepancies between two datasets.

print("")   # Just to add a blank line for better readability of output
print("End of zip() function examples.")
