# Simple math checker
def check_number(number: int) -> list:
    list = []
    if number > 0:
        list.append(True)
    else:
        list.append(False)
    if number % 2 == 0:
        list.append(True)
    else:
        list.append(False)
    if number % 10 == 0:
        list.append(True)
    else:
        list.append(False)
    return list


print(check_number(3))  # [True, False, False]
