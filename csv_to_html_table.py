help_text='''Скрипт конвертирует таблицу в формате csv в html-таблицу.
csv-файл принимается в качестве аргумента скрипта, html-таблица
возвращается в стандарный вывод.

Вызов скрипта:
    python3 csv_to_html_table.py <файл.csv>
'''

import sys
import csv

if len(sys.argv) < 2:
    print(help_text);
    exit()

filename=sys.argv[1]

with open(filename, newline='') as csvfile:
    csv = csv.reader(csvfile, delimiter=',', quotechar='"')
    print('<table>')
    header = True
    for row in csv:
        print('  <tr>')
        for col in row:
            if header:
                print('    <th>' + col + '</th>')
            else:
                print('    <td>' + col + '</td>')
        header = False
        print('  </tr>')
    print('</table>')
