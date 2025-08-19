# Example of using underscores for better readability in integers
num1=1_000_000
num2=2_000_000

print("Number 1:", num1)
print("Number 2:", num2)
sum = num1 + num2
print("Sum:", sum)

# Using f-string for formatted output
print("\nUsing f-string for formatted output :")
print("Sum with commas:", f"{sum:,}")  # Using commas for better readability
print("Sum with underscores:", f"{sum:_}")  # Using underscores for better readability
print("Sum with spaces:", f"{sum: }")  # Using spaces for better readability

# Using format method for formatted output
print("\nUsing format method for formatted output:")  
print("Sum with commas:", "{:,}".format(sum))  # Using commas for better readability
print("Sum with underscores:", "{:_}".format(sum))  # Using underscores for better readability
print("Sum with spaces:", "{: }".format(sum))  # Using spaces for better readability
