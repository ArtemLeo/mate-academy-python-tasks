"""
For loops and While loops.

Loop For:
A for loop is used to iterate over a sequence (such as a list, tuple, or string)
or other iterable objects.

  fruits = ["apple", "banana", "cherry"]
  for fruit in fruits:
      print(fruit)

1. range() Function:
The range() function is often used with for loops to generate a sequence of numbers.

  for i in range(5):  # Generates numbers from 0 to 4
     print(i)

2. enumerate() Function:
enumerate() is used to iterate over both the index and the values of a sequence.

  fruits = ["apple", "banana", "cherry"]
  for index, fruit in enumerate(fruits):
      print(f"Index {index}: {fruit}")

3. zip() Function:
zip() is used to combine two or more iterables element-wise.

  fruits = ["apple", "banana", "cherry"]
  colors = ["red", "yellow", "black"]
  for fruit, color in zip(fruits, colors):
      print(f"{fruit} is {color}")

Loop While:
A while loop continues executing as long as a certain condition is True.

  count = 0
  while count < 5:
      print(f"Count: {count}")
      count += 1

Statements:
break: Terminates the loop.
continue: Skips the rest of the loop and continues with the next iteration.
else: is executed when the loop condition becomes False.


Looping Through Dictionaries:
You can iterate through keys, values, or key-value pairs in a dictionary.

 my_dict = {"a": 1, "b": 2, "c": 3}

 # Iterating through keys
   for key in my_dict:
       print(key)

 # Iterating through values
   for value in my_dict.values():
       print(value)

 # Iterating through key-value pairs
   for key, value in my_dict.items():
       print(f"{key}: {value}")

"""
