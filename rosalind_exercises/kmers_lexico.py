import itertools as it

with open('input/test.txt') as f:
    lines = f.readlines()
    alphabet = lines[0].split(' ')
    str_len = int(lines[1])

alphabet = sorted(alphabet)
output = []

str_len = 5

# both of these permutation generators from an earlier rosalind solution "Enumerating Gene Orders"

def permutations_1(l):
    # takes a list object like list(range(1, int+1))
    return [ (m[:i] + [l[0]] + m[i:]) for m in permutations_1(l[1:]) for i in range(len(m)+1) ] if len(l)>1 else [l]

def permutations_2(i):
    # takes an int, returns a list of tuples
    p = it.permutations(range(1,i+1))
    return [j for j in p]



out = permutations_2(4)
print(len(out))