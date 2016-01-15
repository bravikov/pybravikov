help_text='''Шаблон скрипта, который принимает в качестве аргумента файл
и обрабатывает его.

Вызов скрипта:
    python3 file_parser_template.py <файл>
'''

import sys

if len(sys.argv) < 2:
    print(help_text);
    exit()

filename=sys.argv[1]

with open(filename) as f:
    for line in f:
        print(line, end='')
