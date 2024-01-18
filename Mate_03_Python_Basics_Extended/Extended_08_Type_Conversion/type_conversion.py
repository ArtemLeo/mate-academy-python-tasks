"""
Type conversion, also known as type casting, is the process of converting one data type
to another in Python. Python provides several built-in functions for performing type conversion.

1. int() Function:
Used to convert a value to an integer.

2. float() Function:
Used to convert a value to a floating-point number.

3. str() Function:
Used to convert a value to a string.

4. bool() Function:
Used to convert a value to a boolean.

  non_zero_number = 3
  boolean_value = bool(non_zero_number)
  print(boolean_value)  # Output: True

  zero_number = 0
  boolean_value = bool(zero_number)
  print(boolean_value)  # Output: False

5. list(), tuple(), set() Functions:
Used to convert an iterable (e.g., a string or another sequence) to a list, tuple, or set.

  text = "Python"
  list_of_characters = list(text)
  tuple_of_characters = tuple(text)
  set_of_characters = set(text)

  print(tuple_of_characters) # Output: ('P', 'y', 't', 'h', 'o', 'n')
  print(set_of_characters)   # Output: {'P', 'y', 't', 'h', 'o', 'n'}
  print(list_of_characters)  # Output: ['P', 'y', 't', 'h', 'o', 'n']

6. dict() Function:
Used to convert an iterable of key-value pairs to a dictionary.

  pairs = [('a', 1), ('b', 2), ('c', 3)]
  my_dict = dict(pairs)
  print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

7. chr() and ord() Functions:
chr() converts an integer to a character, and ord() converts a character to its Unicode code.

  unicode_code = 65
  character = chr(unicode_code)
  print(character)  # Output: 'A'

  char_A = 'A'
  unicode_value = ord(char_A)
  print(unicode_value)  # Output: 65

8. eval() Function:
Used to evaluate a string expression and return the result.

  expression = "2 + 3"
  result = eval(expression)
  print(result)  # Output: 5



"""
