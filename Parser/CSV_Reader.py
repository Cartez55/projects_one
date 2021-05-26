import csv

with open("CSI диалоги апрель.csv", 'r', newline="",
          encoding='utf-8') as file:
    # Считываем файл, указывая делитель ";"
    reader = csv.DictReader(file, delimiter=';')
    # Проходимся циклом по строке дата
    with open("exp.txt", "w", encoding="UTF-8") as p:
        for row in reader:
            if row["CHAT_TXT"]:
                row_split = row["CHAT_TXT"].split('!.')
                # print(row_split, "\n\n")
                # p.write(row["CHAT_TXT"] + "\n\n")
                bot = []
                human = []
                all_phrase = []
                list_symbols = ['!', '?', '.']
                for symbols in list_symbols:
                    for strings in row_split:
                        if symbols not in strings:
                            print(True)
                            all_phrase.append(human.append(strings))
