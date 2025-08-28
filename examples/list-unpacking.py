# An example of list unpacking in Python
emp_info = ['John', 'Smith', 'IT Dept', 'Developer', 30]
first_name, last_name, *rest = emp_info
print("First name:", first_name)
print("Last name:", last_name)
print("Rest of the items:", rest)

print ("\nAnother example of unpacking:")
first_name, last_name, *rest, age = emp_info
print("First name:", first_name)
print("Last name:", last_name)
print("Age:", age)
