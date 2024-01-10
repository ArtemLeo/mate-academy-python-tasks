# Split string

def split_string(string: str) -> list:
    list = []
    for i in range(0, len(string), 2):
        part = string[i]
        if i + 1 < len(string):
            part += string[i + 1]
        else:
            part += "_"
        list.append(part)
    return list


def split_string_slice(string: str) -> list:
    list = []
    for i in range(0, len(string), 2):
        part = string[i:i + 2]
        if len(part) == 1:
            part += "_"
        list.append(part)
    return list


print(split_string("12345"))  # ["12", "34", "56"]
print(split_string_slice("12345"))  # ["12", "34", "56"]
