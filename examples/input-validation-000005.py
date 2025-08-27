# This code snippet is part of a Python script that validates user input.
# The code demonstrates a simple way to handle user input validation.

def do_this ():
    print("Doing this")

def do_that ():
    print("Doing that")

match input("Enter command: (this/that) ").strip().lower():
    case "this":
        do_this()
    case "that":
        do_that()
    case _:
        print("Unknown command")
