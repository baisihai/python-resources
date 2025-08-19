# This code snippet is part of a Python script that validates user input.
# It prompts the user for their name and assigns a default value if no input is provided.
# The code demonstrates a simple way to handle user input validation.

user_input = input("Enter your name: ")

if user_input:
    user_name = user_input
else:
    user_name = "N/A"

print(f"User Name = {user_name}")
