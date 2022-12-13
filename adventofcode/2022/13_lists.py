# needed tons of help for this one
# big thanks to https://topaz.github.io/paste/#XQAAAQC5BgAAAAAAAAAzHIoib6poHLpewxtGE3pTrRdzrponKxQZYKczHikJjiNFSjdGfrXdLPyRrJ5h+MANbVGHgzyI5M4XtB1qaIjN4dOtojCNC4y0Soxr3R2Nsuiz6eTyUijhgmdC4XKj09b89GKEe5dEldgf5Z3qKfquCJ145VpS1xZg2ZmFgHbGHkhVX7O+XKrVuGKjzTLXFiZmPTe9bJg12VLsYjVo6x8EvdWug+5ZyTA5FE3BT3CCBNxeWqj4cLV6XrcV0Qt782q7Wk56YRxr3gVtudBsbXkCggcql0kZSnwKJthvppx4G6/MR773P1n568zlx4A75JB26AII/iLZcSa8Sq/VYF6V3ZfVAtuwkfOc2vWics53WjEMzE+noC7xx4ZgS2/PhPQL/lLxLmiort6Go3NJHBlH3C0IlqoWv8MV//AZX/DtS5oJIsgQlNs7JntnnN9Ol7pK+diBU6hkX1x+R7tHWgath05261NKl5CsOUZcfQDcKwQTvgAkLTbKmtzmD5y1uMniI0ymw99As/ij6paBjbyCrpKUT9SNRBo3PY7jjnopOqUnElVY3L//D/+wgpMDHcTLJ4MbD2ehqvNJhNZOHqOW5p0uDI9l2cKTFXROpCGURCMDiZXjM2S+orJ9oum2fDeHR8vH0kuwmaoE0ny80WwcykpxuHXeAI5UwSlxXsGXIdxSlvCjtcQm3qH3R70n1jqpQ1/Z1bigdOOId7gUi02qdg+DJVtyZagBsW45h+3nQ4SevhwtHVdYmgBvaCUhuT93z/q1BNnskj6UOgIZ/q8cyXozgbtLJecMSvH+lLCg

import functools

def process_input(fname, part2=False):
    pairs = [] if not part2 else [[[2]], [[6]]]
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        for line_num in range(0,len(lines),3):
            list1 = eval(lines[line_num])
            list2 = eval(lines[line_num+1])

            if not part2:
                pairs.append([list1, list2])
            else:
                pairs.append(list1)
                pairs.append(list2)
    
    return pairs

def compare_pairs(l1, l2):

    # loop through lists by index, since len might be diff
    max_len = max(len(l1), len(l2))
    for idx in range(max_len):
        # check if list lens are different
        if idx == len(l1) and idx < len(l2):  # i.e., we are at the end of l1 but still have some l2
            return True
        if idx == len(l2) and idx < len(l1):
            return False
        
        i1, i2 = l1[idx], l2[idx]

        # both i1 and i2 are ints:
        if isinstance(i1, int) and isinstance(i2, int):
            if i1 < i2:
                return True
            elif i1 > i2:
                return False
            elif i1 == i2:
                continue
        
        # both i1 and i2 are lists:
        elif isinstance(i1, list) and isinstance(i2, list):
            ans = compare_pairs(i1, i2)
            if ans is not None:
                return ans
        
        # i1/i2 are list/int (or vice versa)
        elif isinstance(i1, int) and isinstance(i2, list):
            ans = compare_pairs([i1], i2)
            if ans is not None:
                return ans

        elif isinstance(i1, list) and isinstance(i2, int):
            ans = compare_pairs(i1, [i2])
            if ans is not None:
                return ans
    
    return None

def main1(fname):
    pairs = process_input(fname)
    ans = 0
    for idx, pair in enumerate(pairs):
        l1, l2 = pair
        if compare_pairs(l1, l2):
            ans += idx + 1

    return ans

# print(main1('input/test.txt'))
print(main1('input/13.txt'))

def main2(fname):
    pairs = process_input(fname, part2=True)

    def sort_all_input(a, b):
        if compare_pairs(a, b):
            return -1
        return 1
    
    sorted_pairs = sorted(pairs, key=functools.cmp_to_key(sort_all_input))

    return (sorted_pairs.index([[2]]) + 1) * (sorted_pairs.index([[6]]) + 1)

# print(main2('input/test.txt'))
print(main2('input/13.txt'))
