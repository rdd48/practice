import itertools as it

n = 6

def permutations(i):
    # takes an int, returns a list of tuples
    p = it.permutations(range(1 , i+1))
    return [j for j in p]

perm_out = permutations(n)
for p in perm_out:
    print(' '.join([str(i) for i in list(p)]))