# Purpose: Remove duplicates from a list while maintaining order

old=['a','b','c','a','b','d']
print("Original list:", old)

# Method 1: Using a loop and a set to track seen items
print("\nMethod 1: Using loop and set")
new1=[] 
seen=set()
for item in old:
    if item not in seen:
        new1.append(item)
        seen.add(item)  
print("List after removing duplicates:", new1)

# Method 2: Using a loop and the new list only
print("\nMethod 2: Using loop and set")
new2=[] 
for item in old:
    if item not in new2:
        new2.append(item)
print("List after removing duplicates:", new2)

# Method 3: Using a dictionary. 
# This is a clever way to remove duplicates
# as dictionaries maintain insertion order in Python 3.7+
print("\nMethod 3: Using dictionary")
new3=list(dict.fromkeys(old))
print("List after removing duplicates:", new3)
