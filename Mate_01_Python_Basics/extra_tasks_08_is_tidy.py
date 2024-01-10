# Is tidy
def is_tidy(number: int) -> bool:
    string = str(number)
    for i in range(len(string) - 1):
        if int(string[i]) > int(string[i + 1]):
            return False
    return True


print(is_tidy(12))  # True
