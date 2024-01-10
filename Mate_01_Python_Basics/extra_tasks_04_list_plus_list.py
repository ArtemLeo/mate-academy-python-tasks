# List plus list
def get_lists_sum(ls1: list, ls2: list) -> int:
    total = 0
    total_list = ls1 + ls2
    if len(total_list) == 0:
        return 0
    for i in range(len(total_list)):
        total += total_list[i]
    return total


print(get_lists_sum([1, 2], [3, 4]))  # 1 + 2 + 3 + 4 = 10
