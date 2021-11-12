from protein_mw import mw_dict

def reverse_and_round_dict(d):
    new_dict = {}
    for k,v in d.items():
        new_k = round(v, 2)
        new_dict[new_k] = k
    return(new_dict)

rev_dict = reverse_and_round_dict(mw_dict)
aas = ''

with open('input/rosalind_spec.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if i < (len(lines) - 1):
            mw_diff = round(float(lines[i+1]) - float(lines[i]), 2)
            aas += rev_dict[mw_diff]
    print(aas)
