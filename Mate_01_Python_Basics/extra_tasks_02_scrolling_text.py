# Scrolling text
def scrolling_text(string: str) -> list:
    list = []
    for i in range(len(string)):
        part = string[i:] + string[:i]
        list.append(part.upper())
    return list


print(scrolling_text('robot'))
