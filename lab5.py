import re

# --------Задание 1------
with open('task1-en.txt', 'r') as file:
    data = file.read()
    rez1 = re.findall(r'\b\w+\b,', data)
    rez1_1 = re.findall(r"\[([^]]*)\]", data)

# --------Задание 2------
with open('task2.html', 'r', encoding='utf-8') as file2:
    rez2 = []
    for line in file2:
        if len((temp := re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}", line))) > 0:
            rez2.append(temp)

print(rez2)