from functools import cache

def generate_all_perms(c):
    perms, new_perms = [c], []
    while True:
        new_perms = []
        for c in perms:
            for idx, i in enumerate(c):
                if i == '?':
                    new_perms.append(c[:idx] + '.' + c[idx+1:])
                    new_perms.append(c[:idx] + '#' + c[idx+1:])
                    break

        if not len(new_perms):
            return perms
        
        perms = new_perms
    
def get_ordered_list(p):
    l = []
    curr = 0
    for i in p + '.':
        if i == '#':
            curr += 1
        elif curr > 0:
            l.append(curr)
            curr = 0
    return l

def check_perms(perms, r):
    total = 0
    for p in perms:
        if get_ordered_list(p) == list(r):
            total += 1
    return total

def main(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    # conds is a list of list, sublists are all permutations for each line
    # recs will be a list of lists, sublists are the num #s in order
    conds, recs = [], []
    rd = 0
    for l in lines:
        c, r = l.split()
        conds.append(generate_all_perms(c))
        # print(rd)
        rd += 1
        recs.append([int(i) for i in r.split(',')])
    
    # this brute force approach will not work for part two i'm sure
    ans = 0
    
    for perms, r in zip(conds, recs):
        ans += check_perms(tuple(perms), tuple(r))
        rd += 1
        


    return ans


# https://github.com/fuglede/adventofcode/blob/master/2023/day12/solutions.py
# a different approach, also very helpful

# this is basically just https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/

def convert_input(l):
    c, r = l.split()
    r = [int(i) for i in r.split(',')]
    return ((c+'?')*5)[:-1] + '.', tuple(r*5)

@cache
def recur_match_cases(s, rules):
    # so basically we chop down the list, failing it when possible
    # if we successfully chop everything down, we get a point
    # all points get summed as this gets recursively larger

    # first check if rules remain & deal with that
    if not rules:
        if not s.count('#'):
            return 1
        else:
            return 0

    # next check if there's more string to deal with, but here there'd still be groups
    if not s:
        return 0

    # deal with first char .s here
    def dot():
        return recur_match_cases(s[1:], rules)

    # deal with first char #s here
    def pound():
        # replace substring ?s with #
        curr_rule = rules[0]
        subs = s[:curr_rule].replace('?', '#')

        # return 0 if we don't make a valid result
        if '.' in subs:
            return 0
        
        # if the current rule is longer than our remaining string, it's not valid
        if len(s) < curr_rule:
            return 0

        # here i make a difference from the reddit link
        # because all my strings are padded with a ., i can skip checking if we're at the end
        # return recursive function one char after curr str + curr rule, and go forward one rule

        if s[curr_rule] in '.?':
            return recur_match_cases(s[curr_rule+1:], rules[1:])
        else:
            return 0

    # here's where we call the above . or # functions
    if s[0] == '.':
        total = dot()
    elif s[0] == '#':
        total = pound()
    elif s[0] == '?':
        total = dot() + pound()
    
    return total


def main2(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    total = 0
    for l in lines:
        c, r = convert_input(l)
        total += recur_match_cases(c,r)
    
    return total
    


print(main2('input/12.txt'))