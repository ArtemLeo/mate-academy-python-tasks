"""
Largest
Write a function named max_key that takes a dictionary named my_dictionary as a parameter.
The function should return the key associated with the largest value in the dictionary.

"""


def max_key(my_dictionary: dict):
    max_value = float('-inf')
    result_key = None
    for key, value in my_dictionary.items():
        if value > max_value:
            max_value = value
            result_key = key
    return result_key


print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))  # should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))  # should print "c"
