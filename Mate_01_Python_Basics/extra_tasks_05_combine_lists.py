# Combine lists
def combine_lists(ls1: list, ls2: list) -> list:
    list = []
    for i in range(len(ls1)):
        list.append(ls1[i] + ls2[i])
    return list


print(combine_lists([1, 2, 5], [3, 6, 1]))  # [4, 8, 6]
