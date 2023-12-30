def process_rule(start, wfs, x, m, a, s):
    curr_wf = wfs[start]
    for wf in curr_wf.split(','):
        if ':' in wf:
            rule, res = wf.split(':')
            if eval(rule):
                if res == 'A':
                    return True
                elif res == 'R':
                    return False
                return process_rule(res, wfs, x, m, a, s)
        else:
            if wf[0] == 'A':
                return True
            elif wf[0] == 'R':
                return False
            else:
                return process_rule(wf, wfs, x, m, a, s)
    exit('wtf?')

def main(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    wfs, parts = {}, []
    for l in lines:
        if l.startswith('{'):
            parts.append(l)
        else:
            start,end = l.split('{')
            wfs[start] = end[:-1]
    
    total = 0
    for p in parts:
        # define x m a s
        for v in p[1:-1].split(','):
            if v[0] == 'x':
                x = int(v[2:])
            elif v[0] == 'm':
                m = int(v[2:])
            elif v[0] == 'a':
                a = int(v[2:])
            elif v[0] == 's':
                s = int(v[2:])
            

        if process_rule('in', wfs, x, m, a, s):
            total += (x + m + a + s)
    
    return total

print(main('input/19.txt'))

# https://github.com/knosmos/advent-2023/blob/main/19/19b.py
# used this heavily for part two. recursions and branched trees are clearly things i could learn more about

def make_test(op, val):
    if op == '<':
        return lambda n: n < val
    elif op == '>':
        return lambda n: n > val
    else:
        assert(False)

def part2(fname):
    workflows = {}
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    
    workflows = {}
    for l in lines:
        if not l.startswith('{'):
            start,end = l.split('{')
            rules = []
            for i in end[:-1].split(','):
                if ':' in i:
                    pre, post = i.split(':')
                    rules.append((post, pre[0], make_test(pre[1], int(pre[2:]))))
                else:
                    rules.append(i)
            workflows[start] = rules

    def count_accepted(w_name, x, m, a, s):
        if w_name == 'A':
            return len(x) * len(m) * len(a) * len(s)
        if w_name == 'R':
            return 0
        
        rules = workflows[w_name]

        c = 0

        for r in rules:
            if isinstance(r, tuple):
                dest = r[0]
                var = r[1]
                test = r[2]

                if var == 'x':

                    # so if rule fails, it gets skipped
                    take_x = tuple(filter(test, x))
                    if len(take_x):
                        c += count_accepted(dest, take_x, m, a, s)
                    x = tuple(n for n in x if not test(n))
                elif var == 'm':
                    take_m = tuple(filter(test, m))
                    if len(take_m):
                        c += count_accepted(dest, x, take_m, a, s)
                    m = tuple(n for n in m if not test(n))
                elif var == 'a':
                    take_a = tuple(filter(test, a))
                    if len(take_a):
                        c += count_accepted(dest, x, m, take_a, s)
                    a = tuple(n for n in a if not test(n))
                elif var == 's':
                    take_s = tuple(filter(test, s))
                    if len(take_s):
                        c += count_accepted(dest, x, m, a, take_s)
                    s = tuple(n for n in s if not test(n))
            else:
                c += count_accepted(r, x, m, a, s)

        return c
    
    answer = count_accepted('in',
                        tuple(range(1, 4001)),
                        tuple(range(1, 4001)),
                        tuple(range(1, 4001)),
                        tuple(range(1, 4001)))
    return answer

print(part2('input/19.txt'))