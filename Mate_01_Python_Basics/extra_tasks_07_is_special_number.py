# Is special number
def is_special_number(number: int) -> str:
    str_num = str(number)
    for i in range(len(str_num)):
        if int(str_num[i]) > 5:
            return "NOT!!"
    return "Special!!"


print(is_special_number(38))  # "NOT!!"
