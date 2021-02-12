import csv
import win32com.client as win32

# Открываем файл для чтения
with open("export_1.csv", 'r', newline="", encoding="UTF-8") as fp:
    # Читаем файл с помощью csv.DictReader
    reader = csv.DictReader(fp, delimiter=';')
    # Работа с Outlook
    outlook = win32.Dispatch('Outlook.Application')
    # Создаем письмо
    mail = outlook.CreateItem(0)
    adress_client = ['rvvagner@sberbank.ru;' ' Vishnyakova.Ol.Al1@sberbank.ru;' 'Pinchuk.A.And@sberbank.ru;' 'sysaprykina@sberbank.ru;']
    # Итерацией добавляем в письмо адрессатов
    for i in adress_client:
        mail.To = i
        # print(i)
    # Тема письма
    mail.Subject = 'Автоматическая рассылка. Тест'
    for row in reader:
        # Добавляем строки из поля 'Номер и название SC/FAQ' которые соотвествует Дате
        date = '11.02.2021'
        if row["Дата"] == date:
            # Текст письма
            mail.Body = 'Добрый день!' + '\v' + 'Это автоматическая рассылка!' + "\n\n" + "Изменения в сценариях за " + date + ':' + '\n\n' + \
                        row["Номер и название SC/FAQ"] + '\v' + "____" + "\v\v" + row["Описание изменений"] + '\n\n'
    mail.Send()

