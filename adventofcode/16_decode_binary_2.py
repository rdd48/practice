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


def type_4(bin_str, i):
    sum = ''
    while bin_str[i] == '1':
        sum += bin_str[i+1:i+5]
        i += 5
    sum += bin_str[i+1:i+5]
    i += 5

    return i, get_bin(sum)


def len_id_0(bin_str, i, og_bin_type):

    subpkg = bin_str[i:i+15]
    subpkg_len = get_bin(subpkg)
    i += 15
    end_i = i + subpkg_len
    values = []
    while i < end_i:
        bin_type = get_bin(bin_str[i+3:i+6])
        if bin_type == 4:
            i, final_val = type_4(bin_str, i+6)
            values.append(final_val)
        else:
            i += 6
            type_id = bin_str[i]
            if type_id == '0':
                i, value = len_id_0(bin_str, i+1, bin_type)
                values.append(value)
            elif type_id == '1':
                i, value = len_id_1(bin_str, i+1, bin_type)
                values.append(value)

    final_val = answer(values, og_bin_type)

    return i, final_val


def len_id_1(bin_str, i, og_bin_type):
    subpkg = bin_str[i:i+11]
    subpkg_num = get_bin(subpkg)
    i += 11
    values = []
    for _ in range(subpkg_num):
        bin_type = get_bin(bin_str[i+3:i+6])
        if bin_type == 4:
            i, final_val = type_4(bin_str, i+6)
            values.append(final_val)
        else:
            i += 6
            type_id = bin_str[i]
            if type_id == '0':
                i, value = len_id_0(bin_str, i+1, bin_type)
                values.append(value)
            elif type_id == '1':
                i, value = len_id_1(bin_str, i+1, bin_type)
                values.append(value)
    
    final_val = answer(values, og_bin_type)

    return i, final_val


def answer(values, bin_type):
    if bin_type == 0:
        return sum(values)
    elif bin_type == 1:
        total = 1
        for v in values:
            total *= v
        return total
    elif bin_type == 2:
        return min(values)
    elif bin_type == 3:
        return max(values)
    elif bin_type == 5:
        if values[0] > values[1]:
            return 1
        return 0
    elif bin_type == 6:
        if values[1] > values[0]:
            return 1
        return 0
    elif bin_type == 7:
        if values[0] == values[1]:
            return 1
        return 0


def main_2(filename):
    bin_str = process_input(filename)
    i = 3
    while i < len(bin_str):
        bin_type = get_bin(bin_str[i:i+3])
        if bin_type == 4:
            i, t4 = type_4(bin_str, i+3)
            return t4

        else:
            i += 3
            type_id = bin_str[i]
            if type_id == '0':
                i, value = len_id_0(bin_str, i+1, bin_type)
                return value
            elif type_id == '1':
                i, value = len_id_1(bin_str, i+1, bin_type)
                return value



# print(main_2('input/test.txt'))
print(main_2('input/16_binary_code.txt'))
