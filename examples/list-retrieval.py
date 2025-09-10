'''
Purpose: Example of retrieving items from a list.
This example demonstrates basic list handling in Python.
'''

def retrieve_items_from_list(input_list):
    for item in input_list:
        print(f"Retrieved item: {item}")
    return input_list

def retrieve_odd_indexed_items_from_list(input_list):
    output_list = input_list[1::2]
    return output_list

def retrieve_even_indexed_items_from_list(input_list):
    output_list = input_list[::2]
    return output_list

def retrieve_reversed_items_from_list(input_list):
    output_list = input_list[::-1]
    return output_list

def retrieve_reversed_odd_indexed_items_from_list(input_list):
    reversed_list = input_list[::-1]
    output_list = reversed_list[1::2]
    return output_list

def retrieve_reversed_even_indexed_items_from_list(input_list):
    output_list = input_list[::-2]
    return output_list

input_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon']
              
retrieved_items = retrieve_items_from_list(input_list)
print(f"All items: {retrieved_items}")

retrieved_items = retrieve_odd_indexed_items_from_list(input_list)
print(f"\nAll odd-indexed items: {retrieved_items}")

retrieved_items = retrieve_even_indexed_items_from_list(input_list)
print(f"\nAll even-indexed items: {retrieved_items}")

retrieved_items = retrieve_reversed_items_from_list(input_list)
print(f"\nAll reversed items: {retrieved_items}")

retrieved_items = retrieve_reversed_odd_indexed_items_from_list(input_list)
print(f"\nAll reversed odd-indexed items: {retrieved_items}")

retrieved_items = retrieve_reversed_even_indexed_items_from_list(input_list)
print(f"\nAll reversed even-indexed items: {retrieved_items}")

print("\nProcessing complete.")
