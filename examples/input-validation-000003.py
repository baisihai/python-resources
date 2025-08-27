# This code snippet is part of a Python script that validates user input.
# It prompts the user for a numeric deposit quantity.
# The code demonstrates a simple way to handle user input validation.

balance = 1000
deposit_input = input("Enter deposit quantity: ")
deposit = int(deposit_input) if deposit_input else 0    # If the user presses Enter without typing anything, deposit is set to 0.
balance += deposit
print(f"Balance = {balance}")
