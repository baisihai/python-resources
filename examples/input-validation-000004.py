# This code snippet is part of a Python script that validates user input.
# It prompts the user for a numeric deposit quantity, and validates that it is a number.
# The code demonstrates a simple way to handle user input validation.

balance = 1000

while True:
    deposit_input = input("Enter deposit quantity: ")
    if deposit_input.isdigit():  # Check if the input is a number
        deposit = int(deposit_input)
        break
    else:
        print("Invalid input. Please enter a numeric value.")

balance += deposit
print(f"Balance = {balance}")
