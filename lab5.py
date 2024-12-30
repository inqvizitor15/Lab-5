import re
import csv

# --------Задание 1--------
with open('task1-en.txt', 'r') as file:
    data = file.read()
    rez1 = re.findall(r'\b\w+\b,', data)
    rez1_1 = re.findall(r"\[([^]]*)\]", data)
print(rez1)
print(rez1_1)

# --------Задание 2--------
with open('task2.html', 'r', encoding='utf-8') as file2:
    rez2 = []
    for line in file2:
        if len((temp := re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}", line))) > 0:
            rez2.append(temp)
print(rez2)

# --------Задание 3--------
with open("task3.txt", "r", encoding="utf-8") as file:
    data = file.read()

    id = re.findall(r"\b\d+\b", data)
    name = re.findall(r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b", data)
    email = re.findall(r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}", data)
    date = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", data)
    website = re.findall(r"https?://(?:www\.)?\S+", data)

records = zip(id, name, email, date, website)
with open("rez3.csv", "w", encoding="utf-8", newline="") as csvfile: # заполнение таблицы
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Name", "Email", "Date", "Website"])
    writer.writerows(records)

