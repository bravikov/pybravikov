help_text = '''
    Скрипт конвертирует прерывания из startup-файла на языке ассемблера
    gcc в прерывания startup-файла на языке Си для gcc.

    Результат ввиде файла startup.c.

    Вызов:
        python3 startup_interrupt_converter.py <имя startup-файла>
'''


import sys

if len(sys.argv) != 2:
    print(help_text)
    exit()


''' Анализирует файл filename и возвращает список строк, в которых
определены прерывания. '''
def get_interrupts_lines(filename):
    patterns = (
        '/* External Interrupts */',
        'g_pfnVectors:',
    )
    result = []
    with open(filename, 'r') as f:
        external_interrupts = False
        for line in f:
            line = line.strip()

            match = False
            for pattern in patterns:
                if pattern in line:
                    external_interrupts = True
                    match = True
                    break

            if match:
                continue

            if external_interrupts and len(line) == 0:
                external_interrupts = False
                break

            if external_interrupts:
                result.append(line)

    return result


''' Обрабатывет строки, в которых описаны прерывания, и возвращает
результат ввиде списка со словарями. Словарь содержит поля:
    name - имя прерывания,
    description - описание прерывания ввиде комментария на языке Си.
'''
def get_interrupts(lines):
    result = []
    for line in lines:
        l = line.split()
        interrupt_name = l[1]
        interrupt_description = ' '.join(l[2:])
        result.append({
            'name': interrupt_name,
            'description': interrupt_description,
        })
    return result


''' Возвращает длину максимально длинного имени прерывания. '''
def get_max_interrupt_name_len(interrupts):
    m = 0
    for interrupt in interrupts:
        l = len(interrupt['name'])
        if l > m:
            m = l
    return m


''' Возвращает объявление функций прерываний на языке Си. '''
def get_intterupts_functions(interrupts):
    result = ''
    ml = get_max_interrupt_name_len(interrupts)
    for interrupt in interrupts:
        name = interrupt['name']
        if name == '0':
            continue
        l = len(name)
        space_len = ml - l + 1
        spaces = ' ' * space_len
        s = 'void ' + name + spaces
        s += '(void) __attribute__ ((weak, alias("Default_Handler")));'
        s += '\n'
        result += s
    return result


''' Возвращает массив прерываний '''
def get_intterupts_array(interrupts):
    result = ''
    ml = get_max_interrupt_name_len(interrupts)
    for interrupt in interrupts:
        l = len(interrupt['name'])
        space_len = ml - l + 1
        spaces = ' ' * space_len
        s = interrupt['name'] + ',' + spaces + interrupt['description']
        s += '\n'
        result += s
    return result


''' Основная программа. '''    
startup_filename = sys.argv[1]

lines = get_interrupts_lines(startup_filename)
interrupts = get_interrupts(lines)

with open('startup.c', 'w') as f:
    f.write('Функции:\n\n')
    f.write(get_intterupts_functions(interrupts))
    f.write('\n\nМассив:\n\n')
    f.write(get_intterupts_array(interrupts))
    f.write('\n')
