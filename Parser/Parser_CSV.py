import csv

with open("C:\\Users\\18411029\\Documents\\PythonCourses\\csv\\export_f.csv", 'r', newline="", encoding='utf-8') as file:
    # Считываем файл, указывая делитель ";"
    reader = csv.DictReader(file, delimiter=';')
    # Проходимся циклом по строке дата
    with open("C:\\Users\\18411029\\Documents\\PythonCourses\\csv\\exp.txt", "w", encoding="UTF-8") as p:
        for row in reader:
            # Выводим строки из поля 'Номер и название SC/FAQ' которые соотвествует Дате
            if row["Дата"] == '20.01.2021':
                p.write(row["Номер и название SC/FAQ"] + ' | ' + row["Описание изменений"] + "\n")

