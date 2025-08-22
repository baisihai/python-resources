def merge_arrays(arr1, arr2):
    """
    Merges two sorted arrays into one sorted array.
    
    Parameters:
    arr1 (list): First sorted array.
    arr2 (list): Second sorted array.
    
    Returns:
    list: Merged sorted array.
    """
    merged = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    # Append remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    return merged

# Example usage
if __name__ == "__main__":
    array1 = [1, 3, 5, 7]
    array2 = [2, 4, 6, 8]
    
    result = merge_arrays(array1, array2)
    print("Merged Array:", result)
