# Make stickers

def make_stickers(details_count: int, robot_part: str) -> list:
    list = []
    for i in range(1, details_count + 1):
        list.append(f'{robot_part} detail #{i}')
    return list


print(make_stickers(3, "Body"))
# ["Body detail #1", "Body detail #2", "Body detail #3"]
