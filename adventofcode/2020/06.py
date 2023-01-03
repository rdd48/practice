with open('input/06.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines.append('') # add empty line to get every item read

    ans = 0
    curr = ''
    for l in lines:
        if l:
            curr += l
        else:
            s = set()
            for i in curr:
                s.add(i)
            ans += len(s)
            curr = ''
    print('part one: ', ans)

    # part two
    ans = 0
    curr = []
    for l in lines:
        if l:
            curr.append(set([i for i in l]))
        else:
            if len(curr) == 1:
                ans += len(curr[0])
            else:
                ans += len(curr[0].intersection(*curr[1:]))
            curr = []

    print('part two: ', ans)
    