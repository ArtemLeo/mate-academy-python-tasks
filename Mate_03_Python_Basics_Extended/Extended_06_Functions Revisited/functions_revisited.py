"""
1. Function Definition:
In Python, a function is defined using the def keyword, followed by the function name,
parameters, and a colon. The function body is indented.

# def greet(name):
    print(f"Hello, {name}!")

2. Function Call:
You can call a function by using its name followed by parentheses, and passing arguments
if required.

# greet("Alice")

3. Return Statement:
A function can return a value using the return statement. A function can have no return statement
or multiple return statements.

# def add_numbers(a, b):
#    return a + b
# result = add_numbers(3, 5)
# print(result)  # Output: 8

4. Default Parameters:
You can provide default values for function parameters.

# def greet_with_default(name="Guest"):
#     print(f"Hello, {name}!")
# greet_with_default()    Output: Hello, Guest!
# greet_with_default("Alice")  Output: Hello, Alice!

5. Keyword Arguments:
You can pass arguments to a function using keyword syntax.

# def greet_with_location(name, location):
#     print(f"Hello, {name}! Welcome to {location}.")
# greet_with_location(location="Paris", name="Alice")

6. Variable Number of Arguments:
You can use *args to pass a variable number of non-keyword arguments and **kwargs to pass
a variable number of keyword arguments

# def print_args(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
# print_args(1, "Hello", name="Alice")

7. Lambda Functions:
Lambda functions are anonymous functions defined using the lambda keyword.
They are often used for short, simple operations.

# square = lambda x: x**2
# print(square(4))  # Output: 16

8. Docstrings:
Adding docstrings (triple-quoted strings) to your functions helps document their purpose and usage.

# def multiply(a, b):
#     '''This function multiplies two numbers.'''
#     return a * b

9. Scope:
Variables defined inside a function have local scope, while those defined outside have global scope.
The global keyword can be used to access global variables within a function.

# global_variable = 10
# def print_global_variable():
#     print(global_variable)
# print_global_variable()  # Output: 10


Functions are necessary to structure your code and increase the modularity of your programs



"""
