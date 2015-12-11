''' Обрабатывает строку позиционных обозначений элементов перечня
элементов и возвращает количество элементов.

Для строки "C1, C2, C5...C8, C13, C14, C19" скрипт возвращает:
    1 | C1
    1 | C2
    4 | C5...C8
    1 | C13
    1 | C14
    1 | C19
    Всего: 9

'''

import re

s = input()

n = 0

for ss in s.split(','):
    ss = ss.strip(' \n\t')

    m = re.search('^[а-яА-Яa-zA-Z]+[0-9]+$', ss)
    if m is not None:
        print('1 |', m.group(0))
        n += 1
        continue

    m = re.search(
        '^[а-яА-Яa-zA-Z]+([0-9]+)...[а-яА-Яa-zA-Z]+([0-9]+)$',
        ss
    )
    if m is not None:
        l = int(m.group(1))
        u = int(m.group(2))
        k = u - l + 1
        n += k
        print(k, '|',  m.group(0))
        continue

print('Всего:', n)
