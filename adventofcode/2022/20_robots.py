def mix_list(fname, part2=False):
    with open(fname) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        encryption = 1 if not part2 else 811589153

        # all_lines will be a list of tuples (idx, int) since the input has dupes
        mix_list = []
        for idx, l in enumerate(lines):
            mix_list.append((idx, int(l) * encryption))

    mix_order = mix_list.copy()
    rounds = 1 if not part2 else 10

    for _ in range(rounds):
        for idx, val in mix_order:
            
            # this gets the index of the item to move in our mix_list
            curr_idx = mix_list.index((idx, val))

            # get new index. modulo is cool here because it makes the negative indices positive
            new_idx = (curr_idx + val) % (len(mix_order) - 1)

            # remove the item first
            mix_list.remove((idx, val))

            # add back
            mix_list.insert(new_idx, (idx, val))
    
    # get idx of val == 0
    vals = [val[1] for val in mix_list]
    zero_idx = vals.index(0)

    idx1 = (zero_idx + 1000) % len(vals)
    idx2 = (zero_idx + 2000) % len(vals)
    idx3 = (zero_idx + 3000) % len(vals)

    return vals[idx1] + vals[idx2] + vals[idx3]
        
# print(mix_list('input/test.txt'))
print(mix_list('input/20.txt'))

# print(mix_list2('input/test.txt'))
print(mix_list('input/20.txt', part2=True))