def process_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    output_str = ''
    for ch in lines[0].strip():
        dec_int = int(ch, 16)
        bin_str = bin(dec_int)[2:]
        leading_zeros = (4 - len(bin_str)) * '0'
        output_str += leading_zeros + bin_str

    return output_str


def get_dec(substr):
    return int(substr, 2)


def type_4(bin_str, i):
    sum = ''
    while bin_str[i] == '1':
        sum += bin_str[i+1:i+5]
        i += 5
    sum += bin_str[i+1:i+5]
    i += 5

    return i, get_dec(sum)


def len_id_0(bin_str, i, og_bin_type, version_total):
    subpkg = bin_str[i:i+15]
    subpkg_len = get_dec(subpkg)
    i += 15
    end_i = i + subpkg_len
    values = []
    while i < end_i:
        version_total += get_dec(bin_str[i:i+3])
        bin_type = get_dec(bin_str[i+3:i+6])
        if bin_type == 4:
            i, final_val = type_4(bin_str, i+6)
            values.append(final_val)
        else:
            i += 6
            type_id = bin_str[i]
            if type_id == '0':
                i, value, version_total = len_id_0(bin_str, i+1, bin_type, version_total)
                values.append(value)
            elif type_id == '1':
                i, value, version_total = len_id_1(bin_str, i+1, bin_type, version_total)
                values.append(value)

    final_val = answer(values, og_bin_type)

    return i, final_val, version_total


def len_id_1(bin_str, i, og_bin_type, version_total):
    subpkg = bin_str[i:i+11]
    subpkg_num = get_dec(subpkg)
    i += 11
    values = []
    for _ in range(subpkg_num):
        version_total += get_dec(bin_str[i:i+3])
        bin_type = get_dec(bin_str[i+3:i+6])
        if bin_type == 4:
            i, final_val = type_4(bin_str, i+6)
            values.append(final_val)
        else:
            i += 6
            type_id = bin_str[i]
            if type_id == '0':
                i, value, version_total = len_id_0(bin_str, i+1, bin_type, version_total)
                values.append(value)
            elif type_id == '1':
                i, value, version_total = len_id_1(bin_str, i+1, bin_type, version_total)
                values.append(value)
    
    final_val = answer(values, og_bin_type)

    return i, final_val, version_total


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

def trailing_zeros(substr):
    for s in substr:
        if s != '0':
            return False
        return True

def main_2(filename, part_two=False):
    bin_str = process_input(filename)
    i = 0
    version_total = 0
    while i < len(bin_str):
        version_total += get_dec(bin_str[i:i+3])
        bin_type = get_dec(bin_str[i+3:i+6])
        if bin_type == 4:
            i, t4 = type_4(bin_str, i+6)
            return version_total, t4

        else:
            i += 6
            type_id = bin_str[i]
            if type_id == '0':
                i, value, version_total = len_id_0(bin_str, i+1, bin_type, version_total)
                if part_two:
                    return value
            elif type_id == '1':
                i, value, version_total = len_id_1(bin_str, i+1, bin_type, version_total)
                if part_two:
                    return value
        
        if trailing_zeros(bin_str[i:]):
            return version_total

    return version_total



print(main_2('input/16_binary_code.txt'))
print(main_2('input/16_binary_code.txt', part_two=True))