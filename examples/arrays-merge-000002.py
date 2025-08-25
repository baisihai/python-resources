"""
Purpose:
# 1) Merge arrays in Python
# 2) Remove duplicates
# 3) Sort the merged array in ascending order
"""

def merge_and_sort_arrays(arr1, arr2):
    """
    Merges two arrays, removes duplicates, and sorts the result.
    
    Parameters:
    arr1 (list): First array.
    arr2 (list): Second array.
    
    Returns:
    list: Merged, deduplicated, and sorted array.
    """
    merged = arr1 + arr2  # Merge arrays
    deduplicated = list(set(merged))  # Remove duplicates
    sorted_array = sorted(deduplicated)  # Sort the array
    return sorted_array

#1 Using the + operator
array1 = [1,2,3,3,4,5,6]
array2 = [4,2,4,5,6,1]

merged_array = merge_and_sort_arrays(array1, array2)
print("Merged array:")
print(merged_array)
