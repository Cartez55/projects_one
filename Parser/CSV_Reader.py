import csv
import re

with open("CSI диалоги апрель.csv", 'r', newline="",
          encoding='utf-8') as file:
    # Считываем файл, указывая делитель ";"
    reader = csv.DictReader(file, delimiter=';')
    # Проходимся циклом по строке дата
    with open("exp.txt", "w", encoding="UTF-8") as p:
        for row in reader:
            # search_letter =
            if re.search("[А-Я]", row["CHAT_TXT"]):
                print(row["CHAT_TXT"], "\n")
            # unique_symbols = set(row["CHAT_TXT"])
            # print(unique_symbols)
            # print(re.split('[А-Я]', row["CHAT_TXT"]), "\n\n")
            # print(re.split('!,?,.', row["CHAT_TXT"]), "\n")
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
