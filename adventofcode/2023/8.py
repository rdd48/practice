from math import lcm

def part1(fname):

    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        order = lines[0]
        d = {}
        for l in lines[1:]:
            k = l.split()[0]
            left = l.split()[-2][1:-1]
            right = l.split()[-1][:-1]
            d[k] = (left, right)
    
    sele = 'AAA'
    steps = 0
    while sele != 'ZZZ':
        o = order[steps % len(order)]
        steps += 1
        pos = 0 if o == 'L' else 1
        sele = d[sele][pos]

    return steps

def check_sele_2(sele, order, d):
    steps = 0
    while sele[-1] != 'Z':
        o = order[steps % len(order)]
        steps += 1
        pos = 0 if o == 'L' else 1
        sele = d[sele][pos]

    return steps

def part2(fname):

    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        order = lines[0]
        seles = []
        d = {}
        for l in lines[1:]:
            k = l.split()[0]
            left = l.split()[-2][1:-1]
            right = l.split()[-1][:-1]
            d[k] = (left, right)
            if k[-1] == 'A':
                seles.append(k)
    
    all_steps = []
    for sele in seles:
        steps = check_sele_2(sele, order, d)
        all_steps.append(steps)
    
    return lcm(*all_steps)

print(part1('input/8.txt'))
print(part2('input/8.txt'))

