# WIP: still not working, and inefficient

from process_fasta import process_fasta

names, fasta_dict = process_fasta('input/test.txt')

def align_strs(str1, str2):
    prefix_len, suffix_len = [], []
    prefix, suffix = [], []

    for i in range(len(str1)):

        # prefix case: i.e, align the end of str2 to the front of str1
                

        start = str2[-i-1:]
        end = str1[:i+1]

        if start == end[:len(str2)]:
            prefix.append(str2 + str1[i+1:])

        # suffix case: i.e, align the end of str1 to the front of str2

        start = str1[-i-1:]
        end = str2[:i+1]

        if start[:len(str2)] == end:
            suffix.append(str1 + str2[i+1:])

        return prefix, suffix 



possible_combos = [fasta_dict[names[0]]]

for n in names[1:]:
    print(possible_combos)

    next_combos = []

    seq = fasta_dict[n]

    for p in possible_combos:
        # print(possible_combos, p, seq)
        prefix, suffix = align_strs(seq, p)
        print(prefix, suffix)
    
        if prefix:
            next_combos += prefix
        if suffix:
            next_combos += suffix
    
    possible_combos = next_combos
    # print(min(possible_combos, key=len))

# print(min(possible_combos, key=len))