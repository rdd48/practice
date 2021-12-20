'''
thanks to https://vikithedev.eu/aoc/2021/20/ for the help in conceptualizing/visualizing this problem!
'''


def process_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        decoder = lines[0].strip()

        # a will be a list of strs for now
        a = []
        for idx in range(2, len(lines)):
            a.append([i for i in lines[idx].strip()])
    return decoder, a


def pad_array(a, pad_len, round_idx):
    if round_idx % 2 == 0:
        ch = '.'
    else:
        ch = '#'
    a_copy = a.copy()
    for idx, row in enumerate(a):
        padding = [ch] * pad_len
        row_copy = row.copy()
        a_copy[idx] = padding + row_copy + padding
    a = a_copy.copy()

    cols = len(a[0])
    new_row = [[ch] * cols]
    for _ in range(pad_len):
        a = new_row + a + new_row

    return a


def trim_padding(a, pad_len=1):
    a_copy = a.copy()
    # trim top & bottom
    a_trim = a_copy[pad_len: -pad_len]

    # trim sides
    a_trim_copy = a_trim.copy()
    for idx, row in enumerate(a_trim):
        row_copy = row.copy()
        a_trim_copy[idx] = row_copy[pad_len: -pad_len]

    return a_trim_copy


def get_bin_num(r, c, a):
    bin_str = ''
    for i in range(-1, 2):
        for j in range(-1, 2):
            ch = a[r+i][c+j]
            if ch == '.':
                bin_str += '0'
            elif ch == '#':
                bin_str += '1'
            else:
                exit('wtf?')

    return int(bin_str, 2)


def print_array(a):
    for row in a:
        print(''.join(row))
    print('')


def count_spots(a):
    total = 0
    for row in a:
        total += row.count('#')
    return total


def main(filename, loops):
    decoder, a = process_input(filename)
    pad_len = 2

    # print_array(a)

    for round_idx in range(loops):

        a = pad_array(a, pad_len, round_idx)

        rows, cols = len(a), len(a[0])

        if round_idx % 2 == 0:
            new_a = [['#'] * cols] * rows
        else:
            new_a = [['.'] * cols] * rows

        for r in range(1, rows-1):
            for c in range(1, cols-1):
                bin_num = get_bin_num(r, c, a)
                new_pixel = decoder[bin_num]
                new_row = new_a[r].copy()
                new_row[c] = new_pixel
                new_a[r] = new_row

        a_trim = trim_padding(new_a, 1)
        a = a_trim.copy()

    return count_spots(trim_padding(new_a, 1))


# print(main('input/test.txt'))
print(main('input/20_spots.txt', 2))

# print(main('input/test.txt', 50))
print(main('input/20_spots.txt', 50))
