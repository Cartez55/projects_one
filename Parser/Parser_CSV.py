import csv
import win32com.client as win32

with open("C:\\Users\\18411029\\Documents\\PythonCourses\\csv\\export_f.csv", 'r', newline="", encoding='utf-8') as file:
    # Считываем файл, указывая делитель ";"
    reader = csv.DictReader(file, delimiter=';')
    # Проходимся циклом по строке дата
    with open("C:\\Users\\18411029\\Documents\\PythonCourses\\csv\\exp.csv", "w", encoding="UTF-8", newline="") as p:
        fieldnames = ['Номер и название SC/FAQ', 'Описание изменений']
        writer = csv.DictWriter(p, fieldnames=fieldnames, delimiter=';')
        for row in reader:
            # Выводим строки из поля 'Номер и название SC/FAQ' которые соотвествует Дате
            if row["Дата"] == '03.02.2021':
                # writer.writeheader()
                writer.writerow([row["Номер и название SC/FAQ"], row["Описание изменений"]])

# outlook = win32.Dispatch('Outlook.Application')
# # mail = outlook.CreateItem(0)
# # mail.To = 'rvvagner@sberbank.ru'
# # mail.Subject = 'Тест. Тест'
# # with open("C:\\Users\\18411029\\Documents\\PythonCourses\\csv\\exp.csv", 'r', newline="", encoding='utf-8') as fp:
# #     read = csv.reader(fp)
# #     mail.Body = read
# # mail.Send()
