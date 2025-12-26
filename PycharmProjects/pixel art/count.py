def count_array(x):
    lines = 0
    for i in x:
        lines += 1
        count = 0
        for _ in i:
            count += 1
        print(count, 'characters')
    print(lines, 'lines')




layout = [
    ['BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'BKG'],
    ['BKG', 'BKG', 'BKG', 'BKG', 'S', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'BKG'],
    ['BKG', 'BKG', 'BKG', 'S', 'S', 'H', 'L', 'H', 'L', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'S', 'S', 'S', 'H', 'L', 'H', 'L', 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'S', 'S', 'T', 'B', 'B', 'B', 'B', 'B', 'T', 'T', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'BKG', 'S', 'S', 'S', 'S', 'S', 'S', 'BKG', 'BKG', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'BKG'],
    ['BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG'],
]





count_array(layout)