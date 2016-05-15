help_text='''
Скрипт заменяет контакты в программе Zoiper контактами из CSV-файла.
Для старых контактов создается резервная копия.

В качестве аргументов принимаются файлы в формате CSV. Первая строка
файла - заголовок. Заголовок может содержать следующие колонки: Имя,
Отчество, Фамилия, Сотовый, Рабочий телефон, Домашний телефон. Регистр
важен.

Если вызвать скрипт без аргументов, то с помощью графического интерфейса
будет запрощен файл.

Вызов скрипта с аргументов -h или --help дает справку.

Работает в операционных системах Linux и Windows 7 и старше.

Синтаксис вызова скрипта:
    python3 zoiper_contacts.py [-h|--help] [файл...]
'''

import sys
import csv
from tkinter.filedialog import *
import datetime
import shutil

if len(sys.argv) == 1:
    op = askopenfilename()
    if len(op) == 0:
        exit()
    filenames = []
    filenames.append(op)
else:
    a1 = sys.argv[1]
    if a1 == '--help' or a1 == '-h':
        print(help_text)
        exit()
    filenames=sys.argv[1:]

if sys.platform == 'linux':
    zoiper_dir = os.path.join(os.getenv('HOME'), '.Zoiper')
elif sys.platform == 'win32':
    zoiper_dir = os.path.join(os.getenv('APPDATA'), 'Zoiper')
else:
    zoiper_dir = ''

xmlfilename = os.path.join(zoiper_dir, 'Contacts.xml')

# Сделать резервную копию.
time = datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
backup = '{}_{}'.format(xmlfilename, time)
shutil.copy(xmlfilename, backup)

xmlfile = open(xmlfilename, 'w')

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
