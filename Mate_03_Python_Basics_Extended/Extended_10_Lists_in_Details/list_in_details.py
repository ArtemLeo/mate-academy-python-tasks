"""
Lists in Python are versatile and widely used for storing collections of items.
A list is a mutable, ordered sequence that can contain elements of different data types.

1. Creating Lists:
Lists are created using square brackets [], and elements are separated by commas.

  my_list = [1, 2, 3, "apple", "banana", True]

2. Accessing Elements:
You can access elements of a list using indexing. Indexing starts at 0 for the first element.

  first_element = my_list[0]
  second_element = my_list[1]
  last_element = my_list[-1]

3. Slicing Lists:
You can extract a portion of a list using slicing.

  sublist = my_list[2:5]  # Elements at index 2, 3, and 4

4. Modifying Lists:
Lists are mutable, meaning you can change their elements.

  my_list[0] = 10  # Modify the first element
  my_list.append("orange")  # Add an element to the end
  my_list.extend([4, 5, 6])  # Add multiple elements to the end
  my_list.insert(2, "pear")  # Insert an element at a specific index

5. Removing Elements:

  my_list.remove("apple")  # Remove a specific element
  popped_element = my_list.pop()  # Remove and return the last element
  del my_list[2]  # Remove an element by index

6. List Operations:

  length = len(my_list)  # Get the length of the list
  sorted_list = sorted(my_list)  # Return a new sorted list
  reversed_list = reversed(my_list)  # Return a new reversed list

7. List Comprehensions:
List comprehensions provide a concise way to create lists.

  squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

8. Nested Lists:
Lists can contain other lists, creating nested structures.

  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

9. Common List Methods:
count(): Count occurrences of an element.
index(): Return the index of the first occurrence of an element.
clear(): Remove all elements from the list.
copy(): Create a shallow copy of the list.
reverse(): Reverse the order of elements in the list.

10. List Membership:
Check if an element is present in a list.

  is_apple_present = "apple" in my_list
  is_mango_absent = "mango" not in my_list






"""