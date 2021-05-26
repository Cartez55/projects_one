import csv
import re

with open("CSI диалоги апрель.csv", 'r', newline="",
          encoding='utf-8') as file:
    # Считываем файл, указывая делитель ";"
    reader = csv.DictReader(file, delimiter=';')
    # Проходимся циклом по строке дата
    with open("exp.txt", "w", encoding="UTF-8") as p:
        for row in reader:
            if row["CHAT_TXT"]:
                # unique_symbols = set(row["CHAT_TXT"])
                # print(unique_symbols)
                # print(row["CHAT_TXT"].split('!,?'), "\n\n")

                # print(re.split('!,?,.', row["CHAT_TXT"]), "\n\n")
                # p.write(row["CHAT_TXT"] + "\n\n"
                bot = []
                human = []
                all_phrase = []
                for strings in row["CHAT_TXT"]:
                    if len(strings) > 40:
                        bot.append(strings)
                    else:
                        human.append(strings)
            # print(bot, "\n")
