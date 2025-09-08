# Purpose: Demonstrate any() function usage in Python.
# The any() function returns True if any element of the iterable is true. If the iterable is empty, it returns False.
# This example checks if any number in a list is greater than 10.
numbers = [1, 5, 8, 12, 3]
result = any(num > 10 for num in numbers)
print(f"Is there any number greater than 10? {result}")
# Output: Is there any number greater than 10? True

# You can also use any() with other iterables like strings or tuples.
strings = ["apple", "banana", "cherry"]
result = any("a" in s for s in strings)
print(f"Is there any string containing 'a'? {result}")
# Output: Is there any string containing 'a'? True

# Example with an empty iterable
empty_list = []
result = any(empty_list)
print(f"Is there any element in the empty list? {result}")
# Output: Is there any element in the empty list? False

# Example with all False values
all_false = [0, "", None, False]
result = any(all_false)
print(f"Is there any True value in all_false list? {result}")
# Output: Is there any True value in all_false list? False

# Example with mixed values
mixed_values = [0, "", None, True, 5]
result = any(mixed_values)
print(f"Is there any True value in mixed_values list? {result}")
# Output: Is there any True value in mixed_values list? True

# Example with a tuple
mixed_tuple = (0, "", None, False, "Hello")
result = any(mixed_tuple)
print(f"Is there any True value in mixed_tuple? {result}")
# Output: Is there any True value in mixed_tuple? True

# Example with a set
mixed_set = {0, "", None, False, 42}
result = any(mixed_set)
print(f"Is there any True value in mixed_set? {result}")
# Output: Is there any True value in mixed_set? True

# Example with a dictionary (checks keys)
mixed_dict = {0: "zero", "": "empty", None: "none", False: "false", True: "true"}
result = any(mixed_dict)
print(f"Is there any True key in mixed_dict? {result}")
# Output: Is there any True key in mixed_dict? True

# Example with a generator expression
gen_exp = (x > 10 for x in [1, 5, 8, 12, 3])
result = any(gen_exp)
print(f"Is there any number greater than 10 in generator expression? {result}")
# Output: Is there any number greater than 10 in generator expression? True

# Example with a custom object
class CustomObj:
    def __init__(self, value):
        self.value = value
    def __bool__(self):
        return self.value > 0
custom_objects = [CustomObj(0), CustomObj(-1), CustomObj(5)]
result = any(custom_objects)
print(f"Is there any CustomObj with value > 0? {result}")
# Output: Is there any CustomObj with value > 0? True

# Example with nested iterables
nested_list = [[0, "", None], [False, 1], [2, 3]]
result = any(any(sublist) for sublist in nested_list)
print(f"Is there any True value in nested_list? {result}")
# Output: Is there any True value in nested_list? True

# Example with all elements False in nested iterables
nested_all_false = [[0, "", None], [False, 0], [None, ""]]
result = any(any(sublist) for sublist in nested_all_false)
print(f"Is there any True value in nested_all_false? {result}")
# Output: Is there any True value in nested_all_false? False

# Example with a large iterable
large_list = [0] * 1000000 + [1]
result = any(large_list)
print(f"Is there any True value in large_list? {result}")
# Output: Is there any True value in large_list? True

# Example with a list of booleans
bool_list = [False, False, True, False]
result = any(bool_list)
print(f"Is there any True value in bool_list? {result}")
# Output: Is there any True value in bool_list? True

# Example with a list of strings
string_list = ["", "", "Hello", ""]
result = any(string_list)
print(f"Is there any non-empty string in string_list? {result}")
# Output: Is there any non-empty string in string_list? True

# Example with a list of numbers
number_list = [0, 0.0, -1, 2]
result = any(number_list)
print(f"Is there any non-zero number in number_list? {result}")
# Output: Is there any non-zero number in number_list? True

# Example with a list of None values
none_list = [None, None, None]
result = any(none_list)
print(f"Is there any non-None value in none_list? {result}")
# Output: Is there any non-None value in none_list? False

# Example with a list of mixed types
mixed_list = [0, "", None, False, "Python", 3.14]
result = any(mixed_list)
print(f"Is there any True value in mixed_list? {result}")
# Output: Is there any True value in mixed_list? True

# Example with a list of empty collections
empty_collections = [[], {}, set(), ()]
result = any(empty_collections)
print(f"Is there any non-empty collection in empty_collections? {result}")
# Output: Is there any non-empty collection in empty_collections? False

# Example with a list of non-empty collections
non_empty_collections = [[], {1}, set(), (2,)]
result = any(non_empty_collections)
print(f"Is there any non-empty collection in non_empty_collections? {result}")
# Output: Is there any non-empty collection in non_empty_collections? True

# Example with a list of functions
def func1():
    return False
def func2():
    return True
func_list = [func1, func2]
result = any(f() for f in func_list)
print(f"Is there any function returning True in func_list? {result}")
# Output: Is there any function returning True in func_list? True

# Example with a list of custom objects with __bool__ method
class AnotherCustomObj:
    def __init__(self, value):
        self.value = value
    def __bool__(self):
        return self.value
custom_obj_list = [AnotherCustomObj(False), AnotherCustomObj(True), AnotherCustomObj(False)]
result = any(custom_obj_list)
print(f"Is there any AnotherCustomObj with True value? {result}")
# Output: Is there any AnotherCustomObj with True value? True

# Example with a list of lists
list_of_lists = [[], [0], [1, 2]]
result = any(list_of_lists)
print(f"Is there any non-empty list in list_of_lists? {result}")
# Output: Is there any non-empty list in list_of_lists? True

# Example with a list of tuples
tuple_of_tuples = [(), (0,), (1, 2)]
result = any(tuple_of_tuples)
print(f"Is there any non-empty tuple in tuple_of_tuples? {result}")
# Output: Is there any non-empty tuple in tuple_of_tuples? True

# Example with a list of sets
set_of_sets = [set(), {0}, {1, 2}]
result = any(set_of_sets)
print(f"Is there any non-empty set in set_of_sets? {result}")
# Output: Is there any non-empty set in set_of_sets? True

# Example with a list of dictionaries
dict_of_dicts = [{}, {"key": "value"}, {"another_key": 123}]
result = any(dict_of_dicts)
print(f"Is there any non-empty dictionary in dict_of_dicts? {result}")
# Output: Is there any non-empty dictionary in dict_of_dicts? True

# Example with a list of mixed iterables
mixed_iterables = [[], {}, set(), (), [1], {2}, (3,), {"key": "value"}]
result = any(mixed_iterables)
print(f"Is there any non-empty iterable in mixed_iterables? {result}")
# Output: Is there any non-empty iterable in mixed_iterables? True

# Example with a list of numbers including infinity
import math
number_with_infinity = [0, 1, -1, math.inf]
result = any(number_with_infinity)
print(f"Is there any non-zero number in number_with_infinity? {result}")
# Output: Is there any non-zero number in number_with_infinity? True

# Example with a list of complex numbers
complex_numbers = [0j, 1+2j, 0+0j]
result = any(complex_numbers)
print(f"Is there any non-zero complex number in complex_numbers? {result}")
# Output: Is there any non-zero complex number in complex_numbers? True

# Example with a list of bytes
bytes_list = [b'', b'hello', b'world']
result = any(bytes_list)
print(f"Is there any non-empty bytes in bytes_list? {result}")
# Output: Is there any non-empty bytes in bytes_list? True

# Example with a list of bytearrays
bytearray_list = [bytearray(), bytearray(b'hello')]
result = any(bytearray_list)
print(f"Is there any non-empty bytearray in bytearray_list? {result}")
# Output: Is there any non-empty bytearray in bytearray_list? True

# Example with a list of frozensets
frozenset_list = [frozenset(), frozenset([1, 2])]
result = any(frozenset_list)
print(f"Is there any non-empty frozenset in frozenset_list? {result}")
# Output: Is there any non-empty frozenset in frozenset_list? True

# Example with a list of range objects
range_list = [range(0), range(1, 5)]
result = any(range_list)
print(f"Is there any non-empty range in range_list? {result}")
# Output: Is there any non-empty range in range_list? True

# Example with a list of memoryviews
memoryview_list = [memoryview(b''), memoryview(b'hello')]
result = any(memoryview_list)
print(f"Is there any non-empty memoryview in memoryview_list? {result}")
# Output: Is there any non-empty memoryview in memoryview_list? True

# Example with a list of custom iterable objects
class CustomIterable:
    def __init__(self, items):
        self.items = items
    def __iter__(self):
        return iter(self.items)
custom_iterable_list = [CustomIterable([]), CustomIterable([1, 2, 3])]
result = any(custom_iterable_list)
print(f"Is there any non-empty CustomIterable in custom_iterable_list? {result}")
# Output: Is there any non-empty CustomIterable in custom_iterable_list? True

# Example with a list of generators
def generator1():
    yield from []
def generator2():
    yield from [1, 2, 3]
generator_list = [generator1(), generator2()]
result = any(generator_list)
print(f"Is there any non-empty generator in generator_list? {result}")
# Output: Is there any non-empty generator in generator_list? True

# Example with a list of iterators
iterator_list = [iter([]), iter([1, 2, 3])]
result = any(iterator_list)
print(f"Is there any non-empty iterator in iterator_list? {result}")
# Output: Is there any non-empty iterator in iterator_list? True

# Example with a list of mixed falsy values
falsy_values = [0, 0.0, "", None, False, [], {}, set(), (), range(0)]
result = any(falsy_values)
print(f"Is there any True value in falsy_values? {result}")
# Output: Is there any True value in falsy_values? False

# Example with a list of mixed truthy values
truthy_values = [0, 0.0, "", None, False, [1], {"key": "value"}, {1}, (2,), range(1)]
result = any(truthy_values)
print(f"Is there any True value in truthy_values? {result}")
# Output: Is there any True value in truthy_values? True

# Example with a list of mixed types including custom objects
class YetAnotherCustomObj:
    def __init__(self, value):
        self.value = value
    def __bool__(self):
        return bool(self.value)
mixed_types = [0, "", None, False, YetAnotherCustomObj(0), YetAnotherCustomObj(1)]
result = any(mixed_types)
print(f"Is there any True value in mixed_types? {result}")
# Output: Is there any True value in mixed_types? True

# Example with a list of nested mixed types
nested_mixed = [0, "", None, False, [0, "", None], [1, 2, 3], {"key": "value"}, set()]
result = any(any(sublist) if isinstance(sublist, list) else bool(sublist) for sublist in nested_mixed)
print(f"Is there any True value in nested_mixed? {result}")
# Output: Is there any True value in nested_mixed? True

# Example with a list of mixed types including functions and custom objects
def another_func():
    return True
mixed_with_functions = [0, "", None, False, another_func, YetAnotherCustomObj(0), YetAnotherCustomObj(5)]
result = any(f() if callable(f) else bool(f) for f in mixed_with_functions)
print(f"Is there any True value in mixed_with_functions? {result}")
# Output: Is there any True value in mixed_with_functions? True

# Example with a list of mixed types including generators and custom objects
def another_generator():
    yield from [1, 2, 3]
mixed_with_generators = [0, "", None, False, another_generator(), YetAnotherCustomObj(0), YetAnotherCustomObj(5)]
result = any(any(another_generator()) if hasattr(another_generator(), '__iter__') else bool(f) for f in mixed_with_generators)
print(f"Is there any True value in mixed_with_generators? {result}")
# Output: Is there any True value in mixed_with_generators? True

# Example with a list of mixed types including iterators and custom objects
mixed_with_iterators = [0, "", None, False, iter([1, 2, 3]), YetAnotherCustomObj(0), YetAnotherCustomObj(5)]
result = any(any(iter([1, 2, 3])) if hasattr(iter([1, 2, 3]), '__iter__') else bool(f) for f in mixed_with_iterators)
print(f"Is there any True value in mixed_with_iterators? {result}")
# Output: Is there any True value in mixed_with_iterators? True
