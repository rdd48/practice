'''
this is, without a doubt, the worst and most embarrassing code i ever wrote.
so i don't know anything about binary trees, and i handled this as a string... big mistake. huge.
leaving here for posterity, and hopefully to look back on someday and appreciate how far i've progressed?
'''


def process_input(filename):
    # handle the inputs as strings, not lists?
    hw_inp = []
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            hw_inp.append(l.strip())

    return hw_inp


def add_strlsts(s1, s2):
    return f'[{s1},{s2}]'


def is_str_int(s):
    try:
        return int(s)
    except ValueError:
        return None


def explode(strlst, idx):
    # idx = index of first val in list to be exploded

    idx_corr = 0
    if is_str_int(strlst[idx+1]) is not None:
        idx_corr += 1
        idx_num = strlst[idx:idx+2]
    else:
        idx_num = strlst[idx]

    idx_right_corr = 0
    if is_str_int(strlst[idx+idx_corr+3]) is not None:
        idx_right_corr += 1
        idx_right_num = int(strlst[idx+idx_corr+2:idx+idx_corr+4])
    else:
        idx_right_num = int(strlst[idx+idx_corr+2])

    idx_left = idx
    left_corr, right_corr = 0, 0
    left = 0
    while idx_left > 0:
        idx_left -= 1
        if is_str_int(strlst[idx_left]) is not None:
            if is_str_int(strlst[idx_left-1]) is not None:
                left_corr -= 1
            left = is_str_int(strlst[idx_left]) + int(idx_num)
            if left_corr == -1:
                left = int(strlst[idx_left-1:idx_left+1]) + int(idx_num)
            break

    idx_right = idx + idx_corr + idx_right_corr + 2
    while idx_right < len(strlst) - 1:
        idx_right += 1
        if is_str_int(strlst[idx_right]) is not None:
            right = is_str_int(strlst[idx_right]) + idx_right_num
            if is_str_int(strlst[idx_right+1]) is not None:
                right_corr += 1
                right = is_str_int(
                    strlst[idx_right:idx_right+2]) + idx_right_num

            break

    new_str = ''
    # is our exploding pair to the left or right of its nested pair?
    if strlst[idx-2] == ',':
        # we are second
        if idx_left > 0:
            new_str = strlst[:idx_left + left_corr]
            new_str += str(left)
            new_str += strlst[idx_left+1:idx-1]
            new_str += '0'
        else:
            new_str = strlst[:idx-1]
            new_str += '0'

        if idx_right < len(strlst) - 1:
            new_str += strlst[idx+4+idx_corr+idx_right_corr:idx_right]
            new_str += str(right)
            new_str += strlst[idx_right+right_corr+1:]
        else:
            # new_str += ','
            new_str += strlst[idx+4+idx_corr+idx_right_corr:]

    else:
        # we are first
        if idx_left > 0:
            new_str = strlst[:idx_left + left_corr]
            new_str += str(left)
            new_str += strlst[idx_left+1:idx-1]
            new_str += '0'
        else:
            new_str = strlst[:idx-1]
            new_str += '0'

        if idx_right < len(strlst) - 1:
            new_str += strlst[idx+4+idx_corr+idx_right_corr:idx_right]
            new_str += str(right)
            new_str += strlst[idx_right+right_corr+1:]
        else:
            # new_str += ','
            new_str += strlst[idx+4+idx_corr+idx_right_corr:]

    return new_str


def split_strlst(strlst, idx):
    # idx = index of first digit in >9 num to be split
    int_to_split = int(strlst[idx:idx+2])
    left = int_to_split // 2
    right = int_to_split - left

    new_str = strlst[:idx]
    new_str += f'[{left},{right}]'
    new_str += strlst[idx+2:]

    return new_str


def check_explode(strlst):
    parens = 0
    for idx, ch in enumerate(strlst):
        if ch == '[':
            parens += 1
        elif ch == ']':
            parens -= 1

        if parens > 4:
            return idx + 1
    return False


def check_split(strlst):
    for idx in range(len(strlst) - 1):
        if is_str_int(strlst[idx:idx+2]):
            return idx
    return False


def dont_judge_me(s):
    for idx, ch in enumerate(s):
        if ch == ',':
            if is_str_int(s[idx+1]) is not None:
                return True
            else:
                return False
        elif not (is_str_int(ch)):
            continue
        if ch in '[]':
            return False
    return False


def magnitude(strlst):
    i = 0
    while True:
        if ',' not in strlst:
            return int(strlst)
        i += 1
        if is_str_int(strlst[i]) is not None:
            new_i = i+1

            if not dont_judge_me(strlst[i:]):
                continue

            if i + 3 < len(strlst):
                i_corr = 0
                new_i = i + 1
                while is_str_int(strlst[new_i]) is not None:
                    i_corr += 1
                    new_i += 1

                if is_str_int(strlst[i+i_corr+2]) is not None:
                    i_corr_2 = 0
                    new_i = i + i_corr + 3
                    while is_str_int(strlst[new_i]) is not None:
                        i_corr_2 += 1
                        new_i += 1
                    sub_ans = (3 * int(strlst[i:i+i_corr+1])) + (2 *
                                                                 int(strlst[i+i_corr+2:i+i_corr+i_corr_2+3]))
                    if strlst[i+i_corr+i_corr_2+3] == ',':
                        strlst = f'{strlst[:i-1]}{sub_ans}{strlst[i+i_corr+2+i_corr_2:]}'
                    else:
                        strlst = f'{strlst[:i-1]}{sub_ans}{strlst[i+i_corr+4+i_corr_2:]}'
                    i = 0
                    continue
                else:
                    continue
        elif i > len(strlst) - 3:
            break
        else:
            continue


def main(filename):
    hw_inp = process_input(filename)

    strlst = f'{add_strlsts(hw_inp[0], hw_inp[1])}'
    i = 1
    while i < len(hw_inp):
        # check if we need to explode
        explosion_idx = check_explode(strlst)
        if explosion_idx:
            try:
                strlst = explode(strlst, explosion_idx)
            except:
                print(strlst, explosion_idx)
                exit()
            continue

        split_idx = check_split(strlst)
        if split_idx:
            strlst = split_strlst(strlst, split_idx)
            continue

        i += 1
        if i < len(hw_inp):
            strlst = add_strlsts(strlst, hw_inp[i])

    print(strlst)
    return magnitude(strlst)


def main_2(filename):
    hw_inp = process_input(filename)

    ans = 0

    for i in range(len(hw_inp)):
        for j in range(len(hw_inp)):
            strlst = f'{add_strlsts(hw_inp[i], hw_inp[j])}'
            while True:
                # check if we need to explode
                explosion_idx = check_explode(strlst)
                if explosion_idx:
                    try:
                        strlst = explode(strlst, explosion_idx)
                    except:
                        print(strlst, explosion_idx)
                        exit()
                    continue

                split_idx = check_split(strlst)
                if split_idx:
                    strlst = split_strlst(strlst, split_idx)
                    continue

                curr_mag = int(magnitude(strlst))
                if curr_mag > ans:
                    ans = curr_mag
                print(curr_mag, ans)
                break

    return ans


# print(main('input/test.txt'))
print(main('input/18_snailfish.txt'))
# print(main_2('input/test.txt'))
print(main_2('input/18_snailfish.txt'))
