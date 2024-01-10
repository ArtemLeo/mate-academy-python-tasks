# Is sorted
def is_sorted(box_numbers: list) -> bool:
    if len(box_numbers) == 0:
        return True
    for i in range(len(box_numbers) - 1):
        if box_numbers[i] > box_numbers[i + 1]:
            return False
    return True


def is_sorted_another(box_numbers: list) -> bool:
    list = box_numbers[:]
    list.sort()
    if box_numbers == list:
        return True
    else:
        return False


print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted_another([1, 2, 3, 4, 5]))  # True
