import csv

with open("CSI диалоги апрель.csv", 'r', newline="",
          encoding='utf-8') as file:
    # Считываем файл, указывая делитель ";"
    reader = csv.DictReader(file, delimiter=';')
    # Проходимся циклом по строке дата
    with open("exp.txt", "w", encoding="UTF-8") as p:
        for row in reader:
            # Выводим строки из поля 'Номер и название SC/FAQ' которые соотвествует Дате
            if row["CHAT_TXT"]:
                row_split = row["CHAT_TXT"].split('!.')
                print(row_split, "\n\n")
            # p.write(row["CHAT_TXT"] + "\n\n")
