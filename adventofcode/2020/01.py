with open('input/01.txt') as f:
    lines = f.readlines()

    # part one
    s = set()
    for l in lines:
        curr = int(l.strip())
        s.add(curr)

        target = 2020 - curr
        if target in s:
            print('part 1: ', curr * target)
            
    
    for i in s:
        for j in s:
            target = 2020 - j - i
            if target in s:
                print('part 2: ', i*j*target)
                exit()

