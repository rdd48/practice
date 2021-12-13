with open('input/rosalind_lexf.txt') as f:
    lines = f.readlines()
    nts = lines[0].strip().split(' ')
    nts.sort()
    str_len = int(lines[1])

all_perms = ['']
for i in range(str_len):
    curr = []
    for perm in all_perms:
        for nt in nts:        
            curr.append(perm + nt)

    all_perms = curr

for i in all_perms:
    print(i)