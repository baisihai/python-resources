# Demonstrates how to check if a string is palindrome or not using different approaches

def is_palindrome_using_native_approach(s):
    # s[::-1] is a function which return reverse of a string
    return s == s[::-1]

def is_palindrome_using_predefined_function(s):
    # Using predefined function to reverse string
    rev = ''.join(reversed(s))

    # Check if both string are equal
    if (s == rev):
        return True
    return False

def is_palindrome_using_recursive_method(s):
    s = s.lower() # Convert string to lower case
    strlen = len(s) # Find length of string

    # if string length is less than 2, then it is palindrome
    if strlen < 2:
        return True
    # If s[0] and s[strlen-1] are equal then call is is_palindrome_using_recursive_method() with substring(1,strlen-1)
    elif s[0] == s[strlen - 1]:
        # Recursive call
        return is_palindrome_using_recursive_method(s[1: strlen - 1])
    else:
        return False

def is_palindrome_using_iterative_method(s):
    # Run loop from 0 to len/2
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


# Main code
s = "madam"
#s = "abcd"

print("Test String =", s)

if is_palindrome_using_native_approach(s):
    print("is_palindrome_using_native_approach = Yes")
else:
    print("is_palindrome_using_native_approach = No")

if is_palindrome_using_predefined_function(s):
    print("is_palindrome_using_predefined_function = Yes")
else:
    print("is_palindrome_using_predefined_function = No")

if is_palindrome_using_recursive_method(s):
    print("is_palindrome_using_recursive_method = Yes")
else:
    print("is_palindrome_using_recursive_method = No")

if is_palindrome_using_iterative_method(s):
    print("is_palindrome_using_iterative_method = Yes")
else:
    print("is_palindrome_using_iterative_method = No")

