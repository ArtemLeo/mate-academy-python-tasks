"""
Logical operators are used to perform logical operations on Boolean values (True or False).
The three main logical operators in Python are And, Or, and Not.

1. And:
The and operator returns True if both operands are True, otherwise, it returns False.

2. Or:
The or operator returns True if at least one of the operands is True, otherwise, it returns False.

3. Not:
The not operator returns the negation of the operand.
If the operand is True, not returns False, and vice versa.

4. Chaining Logical Operators:
You can chain multiple logical operators together to create complex conditions.
It's important to understand the order of evaluation and use parentheses to explicitly define
the order when dealing with complex conditions.

  x = True
  y = False
  z = True
  result = x and y or z
  print(result)  # Output: True

5. Truthy and Falsy Values:
In Python, certain values are considered truthy (evaluating to True in a boolean context)
and others are considered falsy (evaluating to False).
For example, 0, None, and empty containers like [] or {} are falsy.

"""