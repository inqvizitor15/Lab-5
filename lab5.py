import re

with open('task1-en.txt', 'r') as file:
    data = file.read()

    #--------Задание 1------
    rez1 = re.findall(r'\b\w+\b,', data)
    rez1_1 = re.findall(r"\[([^]]*)\]", data)

    # --------Задание 2------
    rez2 = re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}", data)

print(rez2)