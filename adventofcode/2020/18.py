# WIP: day 18 has different order of operation rules than default python

with open('input/18.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    ans = 0
    for l in lines:
        ans += eval(l)
    
    print('part one:', ans)