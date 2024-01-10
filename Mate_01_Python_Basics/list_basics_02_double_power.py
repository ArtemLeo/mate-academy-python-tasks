# Double power

def double_power(current_powers: list) -> list:
    list = []
    for i in range(len(current_powers)):
        list.append(current_powers[i] * 2)
    return list


print(double_power([100, 150, 200, 220]))  # [200, 300, 400, 440]
