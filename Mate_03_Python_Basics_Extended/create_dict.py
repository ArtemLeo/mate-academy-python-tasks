"""
Create dict

Write create_dict function, which will receive as many arguments as needed and create a dictionary,
in which keys are these arguments (each argument is different key) provided to the function
and values are the positions of these arguments.

Of course, not all arguments provided will be accepted for dict creation.
Print f"Cannot add {argument} to the dict!" for each argument, that is not accepted.

It is agreed, that arguments provided to create_dict function will be only of next types:
int, float, str, bool, NoneType, list, tuple, set, dict, function.

"""


def create_dict(*args) -> dict:
    result_dict = {}
    for key, value in enumerate(args):
        invalid_type = (list, set, dict)
        if isinstance(value, invalid_type):
            print(f"Cannot add {value} to the dict!")
        else:
            result_dict[value] = key
    return result_dict


print(create_dict(7, 1, 3))  # {7: 0, 1: 1, 3: 2}
print(create_dict(3, [1, 2], 5))  # Cannot add [1, 2] to the dict! {3: 0, 5: 2}
print(create_dict(3, (1, 2), 5))  # {3: 0, (1, 2): 1, 5: 2}
