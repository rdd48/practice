# this was very fun but without a doubt currently the ugliest code i've ever written
# will clean up tomorrow

def process_input(filename, part_one=True):
    digits = []
    if part_one:
        with open(filename) as f:
            lines = f.readlines()
            for l in lines:
                split_l = l.strip().split('|')
                digits.append(split_l[1].split(' '))

        return digits

    else:
        input_digits = []
        output_digits = []
        with open(filename) as f:
            lines = f.readlines()
            for l in lines:
                split_l = l.strip().split('|')
                input_digits.append(split_l[0].strip().split(' '))
                output_digits.append(split_l[1].strip().split(' '))
        return input_digits, output_digits


def main_1(filename):
    digits = process_input(filename)
    num = 0
    for i in digits:
        for j in i:
            if len(j) in [2, 4, 3, 7]:
                num += 1

    return num


def main_2(filename):
    inp_all, outp_all = process_input(filename, part_one=False)

    d = {
        i: 'x' for i in 'abcdefg'
    }

    total = 0

    for inp_list, outp_list in zip(inp_all, outp_all):
        # first we can get the top by finding 1 (only len 2) and 7 (only len 3).
        # the digit in one but not 7 is top
        # top is stored as 'a' in our dict, since 'a' is the original digit for the top
        for inp in inp_list:
            if len(inp) == 2:
                # right_side = ''.join(sorted(inp))
                right_side = inp
            elif len(inp) == 3:
                seven = inp
                # inp_list.remove(inp) # remove 7
        for i in seven:
            if i not in right_side:
                d[i] = 'a'
                a_val = i

        # now that we have top and right_side
        # if top and right side in inp:
        # could be 0 (len6), 3 (len5), 7/8, or 9 (6)
        # so we know 3 now
        for inp in inp_list:
            if len(inp) == 5:
                if seven[0] in inp and seven[1] in inp and seven[2] in inp:
                    mid_bottom = ''
                    for j in inp:
                        if j not in [right_side[0], right_side[1], a_val]:
                            mid_bottom += j

        # we have top, right, and mid. we can get 'b' aka top right from 9!
        for inp in inp_list:
            if len(inp) == 6:
                if mid_bottom[0] in inp and mid_bottom[1] in inp:
                    if right_side[0] in inp and right_side[1] in inp:
                        # we are at 9 now
                        for i in inp:
                            if i not in [mid_bottom[0], mid_bottom[1], right_side[0], right_side[1], a_val]:
                                d[i] = 'b'
                                b_val = i
                            # inp_list.remove(inp) # remove 9

        # therefore we can find 5 and thus f:
        for inp in inp_list:
            if len(inp) == 5:
                if mid_bottom[0] in inp and mid_bottom[1] in inp and b_val in inp:
                    for i in inp:
                        if i not in [mid_bottom[0], mid_bottom[1], a_val, b_val]:
                            d[i] = 'f'
                            f_val = i

        # get c from 1:
        for i in right_side:
            if i != f_val:
                d[i] = 'c'
                c_val = i

        # get e from 6:
        for inp in inp_list:
            if len(inp) == 6:
                if not (right_side[0] in inp and right_side[1] in inp):
                    if mid_bottom[0] in inp and mid_bottom[1] in inp:
                        if b_val in inp and f_val in inp and a_val in inp:
                            # at 6
                            for i in inp:
                                if i not in [mid_bottom[0], mid_bottom[1], a_val, b_val, f_val]:
                                    d[i] = 'e'
                                    e_val = i

        # get d from 4:
        for inp in inp_list:
            if len(inp) == 4:
                for i in inp:
                    if i not in [b_val, c_val, f_val]:
                        d[i] = 'd'
                        d_val = i

        # finally, get g from mid_bottoms:
        for i in mid_bottom:
            if i != d_val:
                d[i] = 'g'

        # now time to solve!
        d_codes = {
            'abcefg': 0,  # 6
            'cf': 1,  # 2
            'acdeg': 2,  # 5
            'acdfg': 3,   # 5
            'bcdf': 4,  # 4
            'abdfg': 5,  # 5
            'abdefg': 6,  # 6
            'acf': 7,  # 3
            'abcdefg': 8,  # 7
            'abcdfg': 9  # 6
        }

        num_decoded = ''
        for outp in outp_list:
            decoded = ''
            for i in outp:
                decoded += d[i]
            decoded = ''.join(sorted(decoded))

            num_decoded = num_decoded + str(d_codes[decoded])

        total += int(num_decoded)

    return total


# print(main('input/test.txt'))
# print(main_2('input/test.txt'))
# print(main_2('input/8_scramble.txt'))
print(main_2('input/8_scramble.txt'))
