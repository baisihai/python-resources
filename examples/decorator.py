# This code snippet demonstrates the use of a decorator in Python. 
# A decorator is a function that takes another function and extends its behavior without explicitly modifying it.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling the function {func.__name__}")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
