# Demonstrates how to use the eval() function in Python to evaluate expressions.
# The eval() function takes a string expression and evaluates it as a Python expression.
# This can be useful for dynamically executing code or evaluating mathematical expressions.
# However, it should be used with caution as it can execute arbitrary code and pose security risks
# if the input is not controlled.
# Example usage of eval() function
expression = "3 * (4 + 5)"
result = eval(expression)
print(f"The result of the expression '{expression}' is: {result}")
# Output: The result of the expression '3 * (4 + 5)' is: 27


# Another example with variables
x = 10
y = 20
expression_with_vars = "x + y"
result_with_vars = eval(expression_with_vars)
print("")   # Just to add a blank line for better readability of output
print(f"The result of the expression '{expression_with_vars}' with x={x} and y={y} is: {result_with_vars}")
# Output: The result of the expression 'x + y' with x=10 and y=20 is: 30
# Note: Be cautious when using eval() with untrusted input, as it can lead to security vulnerabilities. 
# Always validate or sanitize input before using eval() in production code.
