import itertools as it

n = 6

def permutations(i):
    # takes an int, returns a list of tuples
    p = it.permutations(range(1 , i+1))
    return [j for j in p]

print(permutations(n))