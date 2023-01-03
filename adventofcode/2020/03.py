with open('input/03.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    # store trees as tuples (row, col) in a set
    all_trees = set()
    for ridx, l in enumerate(lines):
        for cidx, char in enumerate(l):
            if char == '#':
                all_trees.add((ridx, cidx))
    
    # part one: we go right 3, down 1. 
    # since this repeats, we can % current col by num cols
    trees = 0
    cols = len(lines[0])
    col = 0
    for row in range(1,len(lines)):
        col = (col + 3) % cols
        if (row, col) in all_trees:
            trees += 1
    
    print('part one: ', trees)

    # part two, same idea, but for different row lens
    r1, r5, r7, r1d2 = 0,0,0,0
    tr1, tr5, tr7, tr1d2 = 0,0,0,0
    for row in range(1,len(lines)):
        r1 = (r1 + 1) % cols
        r5 = (r5 + 5) % cols
        r7 = (r7 + 7) % cols

        if (row, r1) in all_trees:
            tr1 += 1
        if (row, r5) in all_trees:
            tr5 += 1
        if (row, r7) in all_trees:
            tr7 += 1
    
    for row in range(2, len(lines), 2):
        r1d2 = (r1d2 + 1) % cols
        if (row, r1d2) in all_trees:
            tr1d2 += 1
    
    print('part two: ', tr1 * trees * tr5 * tr7 * tr1d2)




