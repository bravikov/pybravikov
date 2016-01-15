table_data = []
try:
    while True:
        row_data = input().split('\t')
        table_data.append(row_data)
except EOFError:

    # Определить ширину колонок

    column_sizes = []
    for row_data in table_data:
        l1 = len(row_data)
        l2 = len(column_sizes)
        if l2 < l1:
            for i in range(l1 - l2):
                column_sizes.append(0)
        for i in range(l1):
            l3 = len(row_data[i])
            if column_sizes[i] < l3:
                column_sizes[i] = l3

    # Сформировать таблицу

    result = ''
    indent = 1

    def separator(column_sizes):
        r = ''
        for column_size in column_sizes:
            r += '+' + '-' * (column_size + 2 * indent)
        if len(r) > 0:
            r += '+\n'
        return r

    result += separator(column_sizes)

    header = False
    if len(table_data) > 1:
        header = True
    
    for r in range(len(table_data)):
        row_data = table_data[r]
        for c in range(len(column_sizes)):
            data = ''
            if c < len(row_data):
                data = row_data[c]
            result += '|'
            result += ' ' * indent
            result += data
            result += ' ' * (column_sizes[c] - len(data))
            result += ' ' * indent
        result += '|\n' 
        if header:
            header = False
            result += separator(column_sizes)

    result += separator(column_sizes)

    print(result)
