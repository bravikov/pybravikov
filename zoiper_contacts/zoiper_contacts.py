help_text='''
Скрипт генерирует xml-файл контактов для программы Zoiper.

В качестве аргументов принимаются файлы в формате CSV. Первая строка
файла - заголовок. Заголовок может содержать следующие колонки: Имя,
Отчество, Фамилия, Сотовый, Рабочий телефон, Домашний телефон. Регистр
важен.

В резульате скрипт создает файл Contacts.xml в текущей папке.

Если вызвать скрипт без аргументов, то будет выведена эта справка.

Вызов скрипта:
    python3 zoiper_contacts.py [файл...]
'''

import sys
import csv

if len(sys.argv) < 2:
    print(help_text);
    exit()

filenames=sys.argv[1:]

xmlfile = open('Contacts.xml', 'w')

xmlfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
xmlfile.write('<contacts>\n')

for filename in filenames:
    with open(filename) as csvfile:
        content = csvfile.read()
        if len(content) == 0:
            continue
        dialect = csv.Sniffer().sniff(content)
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)

        def value(row, col_name):
            try:
                v = row[col_name].strip()
            except KeyError:
                v = ''
            return v

        for row in reader:
            first_name = value(row, 'Имя')
            last_name = value(row, 'Фамилия')
            middle_name = value(row, 'Отчество')
            home_phone = value(row, 'Домашний телефон')
            work_phone = value(row, 'Рабочий телефон')
            cell_phone = value(row, 'Сотовый')

            display = "{} {} {}".format(first_name, middle_name, last_name)
            display = display.strip().replace('  ', ' ')

            xmlfile.write('  <contact>\n')
            contact = ''
            contact += '    <display>{}</display>\n'.format(display)
            contact += '    <first_name>{}</first_name>\n'.format(first_name)
            contact += '    <last_name>{}</last_name>\n'.format(last_name)
            contact += '    <middle_name>{}</middle_name>\n'.format(middle_name)
            contact += '    <home_phone>{}</home_phone>\n'.format(home_phone)
            contact += '    <work_phone>{}</work_phone>\n'.format(work_phone)
            contact += '    <cell_phone>{}</cell_phone>\n'.format(cell_phone)
            xmlfile.write(contact)
            xmlfile.write('  </contact>\n')

xmlfile.write('</contacts>\n')
xmlfile.close()
