# Get location
def get_location(coordinates: list, commands: list) -> list:
    for i in range(len(commands)):
        if commands[i] == "forward":
            coordinates[1] += 1
        elif commands[i] == "back":
            coordinates[1] -= 1
        elif commands[i] == "right":
            coordinates[0] += 1
        elif commands[i] == "left":
            coordinates[0] -= 1
    return coordinates


print(get_location([2, 3], ["back", "back", "back", "right"]))  # [3, 0]
