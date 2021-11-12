'''
Much thanks to the below link for help in solving this!
http://saradoesbioinformatics.blogspot.com/2016/07/introduction-to-random-strings.html
'''

import math

with open('input/rosalind_prob.txt') as f:
    lines = f.readlines()
    dna_seq = lines[0]
    gc_list = lines[1].split(' ')
    
gc_list = [float(gc) for gc in gc_list]

def count_at_gc(seq):
    at, gc = 0, 0
    for i in seq:
        if i in ['A', 'T']:
            at += 1
        elif i in ['G', 'C']:
            gc += 1
    return at, gc

at, gc = count_at_gc(dna_seq)

prob_list = []

for i in range(len(gc_list)):
    prob_at = ((1 - gc_list[i]) / 2) ** at
    prob_gc = (gc_list[i] / 2) ** gc
    prob = math.log10(prob_at) + math.log10(prob_gc)
    prob_list.append(str(round(prob, 3)))

print(' '.join(prob_list))