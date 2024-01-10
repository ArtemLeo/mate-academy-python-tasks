"""
Values That Are Keys
Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter.
This function should return a list of all values in the dictionary that are also keys.

"""


def values_that_are_keys(my_dictionary: dict) -> list:
    list = []
    for key, value in my_dictionary.items():
        for other_key, other_value in my_dictionary.items():
            if key == other_value:
                list.append(other_value)
    return list


print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))  # should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))  # should print ["a"]
