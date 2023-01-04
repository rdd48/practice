with open('input/10.txt') as f:
    lines = f.readlines()
    lines = [int(l.strip()) for l in lines]
    
    adapters = sorted(lines)

    add1, add3 = (1, 1) if adapters[0] == 1 else (0, 2) # always add the last adapter into add3
    for idx, i in enumerate(adapters[1:]):
        prev = adapters[idx] # idx one lower than curr since we started at element 1
        if i - prev == 1:
            add1 += 1
        elif i - prev == 3:
            add3 += 1
    
    print('part one: ', add1 * add3)

    # part two
    # just add 0 and the final one immediately and make a set for easy lookup
    adapters = [0] + adapters.copy() + [adapters[-1]+3]

    # do like a bfs? each path is a list.
    # update: way too slow
    # new idea: create a dict of adapter keys and num times visited as values
    # update for each current value
    d = {k:0 for k in adapters}
    d[0] = 1
    
    for a in adapters:
        if a+1 in d:
            d[a+1] += d[a]
        if a+2 in d:
            d[a+2] += d[a]
        if a+3 in d:
            d[a+3] += d[a]
    print('part two: ', d[adapters[-1]])
