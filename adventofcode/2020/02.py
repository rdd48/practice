with open('input/02.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    # part one
    ans = 0
    for l in lines:
        lsplit = l.split()
        pmin, pmax = int(lsplit[0].split('-')[0]), int(lsplit[0].split('-')[1])
        char = lsplit[1][0]
        pword = lsplit[-1]

        char_count = pword.count(char)
        if pmin <= char_count <= pmax:
            ans += 1
    
    print(ans)

    # part two
    ans = 0
    for l in lines:
        lsplit = l.split()
        pmin, pmax = int(lsplit[0].split('-')[0]), int(lsplit[0].split('-')[1])
        char = lsplit[1][0]
        pword = lsplit[-1]

        if (pword[pmin-1] == char) is not (pword[pmax-1] == char):
            ans += 1

    print(ans)
        