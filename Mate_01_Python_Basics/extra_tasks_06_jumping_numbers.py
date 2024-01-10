# Jumping numbers   Other
def is_jumping(number: int) -> str:
    str_num = str(number)
    if len(str_num) == 1:
        return "JUMPING"

    for i in range(len(str_num) - 1):
        if abs(int(str_num[i]) - int(str_num[i + 1])) != 1:
            return "NOT JUMPING"
    return "JUMPING"


def is_jumping_other(number: int) -> str:
    str_num = str(number)
    if len(str_num) == 1:
        return "JUMPING"
    for i in range(len(str_num) - 1):
        part1 = int(str_num[i])
        part2 = int(str_num[i + 1])
        if abs(part1 - part2) != 1:
            return "NOT JUMPING"
    return "JUMPING"


print(is_jumping(23454))  # "JUMPING"
print(is_jumping_other(23454))  # "JUMPING"
