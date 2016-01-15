help_text='''Скрипт перемешивает слова из файла и выдает резульатат в
одну строку. В файле в каждой строке по одному слову.

Вызов скрипта:
    python3 shuffle_words.py <файл>
'''

import sys
from random import shuffle

if len(sys.argv) < 2:
    print(help_text);
    exit()

filename=sys.argv[1]

words = []
with open(filename) as f:
    for line in f:
        words.append(line.strip())

shuffle(words)
print(' '.join(words))
print(len(words))
