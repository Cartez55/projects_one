import csv
import win32com.client as win32

with open("export_r.csv", 'r', newline="", encoding='utf-8') as file:
    # Считываем файл, указывая делитель ";"
    reader = csv.DictReader(file, delimiter=';')
    # Проходимся циклом по строке дата
    r = file
with open("exp.txt", "w", encoding="UTF-8") as p:
    for row in r:
        # Выводим строки из поля 'Номер и название SC/FAQ' которые соотвествует Дате
        if row["Дата"] == '20.01.2021':
            p.write(row["Номер и название SC/FAQ"] + ' | ' + row["Описание изменений"] + "\n")

# outlook = win32.Dispatch('Outlook.Application')
# # mail = outlook.CreateItem(0)
# # mail.To = 'rvvagner@sberbank.ru'
# # mail.Subject = 'Тест. Тест'
# # with open("C:\\Users\\18411029\\Documents\\PythonCourses\\csv\\exp.csv", 'r', newline="", encoding='utf-8') as fp:
# #     read = csv.reader(fp)
# #     mail.Body = read
# # mail.Send()
