"""
EvenKeys
Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values,
as a parameter. This function should return the sum of the values of all even keys.

"""


def sum_even_keys(my_dictionary: dict) -> int:
    sum = 0
    for key, value in my_dictionary.items():
        if key % 2 == 0:
            sum += value
    return sum


print(sum_even_keys({1: 5, 2: 2, 3: 3}))  # should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))  # should print 6
