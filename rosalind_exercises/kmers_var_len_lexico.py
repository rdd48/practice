import random
from typing import final

with open('input/test.txt') as f:
    lines = f.readlines()
    nts = lines[0].strip().split(' ')
    str_len = int(lines[1])

final_perms = []
all_perms = ['']
for _ in range(str_len):
    curr = []
    for perm in all_perms:
        for nt in nts:        
            curr.append(perm + nt)
    
    all_perms = curr
    final_perms += all_perms

sorted_perms = [all_perms[0]]

