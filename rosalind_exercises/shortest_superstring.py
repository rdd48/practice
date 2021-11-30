# WIP: still not working, and inefficient

from process_fasta import process_fasta

names, fasta_dict = process_fasta('input/rosalind_long.txt')

def align_strs(str1, str2):

    prefix, suffix = [], []

    for i in range(len(str1)):

        if str1[:i+1] == str2[-i-1:]:
            prefix.append(str2 + str1[i+1:])
        if str1[-i-1:] == str2[:i+1]:
            suffix.append(str1 + str2[i+1:])
    
    # prefix = min(prefix, key=len) if prefix else None
    # suffix = min(suffix, key=len) if suffix else None

    return prefix, suffix 

possible_combos = [fasta_dict[names[0]]]
curr_combos = []

for n in names[1:]:
    seq = fasta_dict[n]


    for p in possible_combos:
        if seq in p:
            curr_combos.append(p)

        prefix, suffix = align_strs(seq, p)

        if prefix:
            curr_combos += prefix
        if suffix:
            curr_combos += suffix
    
    possible_combos = curr_combos
    curr_combos = []

    print(min(possible_combos, key=len))
