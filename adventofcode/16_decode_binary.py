def process_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    convert = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    bin_str = ''
    for ch in lines[0].strip():
        bin_str += convert[ch]

    return bin_str


def get_bin(substr):
    return int(substr, 2)


def trailing_zeros(substr):
    for s in substr:
        if s != '0':
            return False
        return True


def type_4(bin_str, i):
    sum = ''
    while bin_str[i] == '1':
        sum += bin_str[i+1:i+5]
        i += 5
    # total += get_bin(bin_str[i+1:i+5])
    sum += bin_str[i+1:i+5]
    i += 5

    return i, get_bin(sum)
    # return bin_str, i, total


def len_id_0(bin_str, i, total):
    subpkg = bin_str[i:i+15]
    subpkg_len = get_bin(subpkg)
    i += 15
    end_i = i + subpkg_len
    while i < end_i:
        version = get_bin(bin_str[i:i+3])
        bin_type = get_bin(bin_str[i+3:i+6])
        total += version
        if bin_type == 4:
            i, t4 = type_4(bin_str, i+6)
            return t4
        else:
            i += 6
            type_id = bin_str[i]
            if type_id == '0':
                i, total = len_id_0(bin_str, i+1, total)
            elif type_id == '1':
                i, total = len_id_1(bin_str, i+1, total)

    return i, total


def len_id_1(bin_str, i, total):
    subpkg = bin_str[i:i+11]
    subpkg_num = get_bin(subpkg)
    i += 11
    for _ in range(subpkg_num):
        version = get_bin(bin_str[i:i+3])
        bin_type = get_bin(bin_str[i+3:i+6])
        total += version
        if bin_type == 4:
            i, t4 = type_4(bin_str, i+6)
        else:
            i += 6
            type_id = bin_str[i]
            if type_id == '0':
                i, total = len_id_0(bin_str, i+1, total)
            elif type_id == '1':
                i, total = len_id_1(bin_str, i+1, total)

    return i, total


def main(filename):
    bin_str = process_input(filename)

    i = 3
    total = 0
    while i < len(bin_str):
        version = get_bin(bin_str[:i])
        bin_type = get_bin(bin_str[i:i+3])
        total += version
        if bin_type == 4:
            # bin_str, i, total = type_4(bin_str, i+3, total)
            i, t4 = type_4(bin_str, i+3)

        else:
            i += 3
            type_id = bin_str[i]
            if type_id == '0':
                i, total = len_id_0(bin_str, i+1, total)
            elif type_id == '1':
                i, total = len_id_1(bin_str, i+1, total)

        if trailing_zeros(bin_str[i:]):
            return total

    return total


# print(main('input/test.txt'))
print(main('input/16_binary_code.txt'))
