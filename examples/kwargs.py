'''
Purpose: Demonstrate the use of **kwargs to accept variable keyword arguments in a function.
'''

def func_display_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}" )
    return kwargs

def func_calculate(**kwargs):
    # Example function that sums values of keyword arguments a, b, c, d and e if they exist
    total = 0       
    for key in ['a', 'b', 'c', 'd', 'e']:
        if key in kwargs:
            total += kwargs[key]
    return total

print("Example calls to func with varying keyword arguments:")

print("\nfunc_display_args(a=1, b=2, c=3)")
func_display_args(a=1, b=2, c=3)

print("\nfunc_display_args(a=1, b=2, c=3, d=4)")
func_display_args(a=1, b=2, c=3, d=4)

print("\nfunc_display_args(a=1, c=3, b=2, d=4, e=5)")
func_display_args(a=1, c=3, b=2, d=4, e=5)

print("\nfunc_calculate(a=1, b=2, c=3)")
total = func_calculate(a=1, b=2, c=3)
print(f"Total: {total}")

print("\nfunc_calculate(a=1, b=2, c=3, d=4)")
total = func_calculate (a=1, b=2, c=3, d=4)
print(f"Total: {total}")

print("\nfunc_calculate(a=1, c=3, b=2, d=4, e=5)")
total = func_calculate (a=1, c=3, b=2, d=4, e=5)
print(f"Total: {total}")
