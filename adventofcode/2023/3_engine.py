def isint(char):
    if char in '0123456789':
        return True
    return False

def get_full_num(idx, l):
    full_num = ''
    for i in l:
        if isint(i):
            full_num += i
        else:
            break
    return int(full_num), idx + len(full_num) - 1

def get_neighbors(x0, x1, y):
    nbs = set()
    nbs.add((x0-1, y))
    nbs.add((x1+1,y))
    for x in range(x0-1, x1+2):
        nbs.add((x,y-1))
        nbs.add((x,y+1))
    return nbs

def part1(fname):
    total = 0
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

        # nums is a list of [x0, x1, y, value] lists
        nums = []

        # symbols is a set of (x,y) tuples of each symbol's location
        symbols = set()

        for row, l in enumerate(lines):
            idx = 0
            while idx < len(l):
                if isint(l[idx]):
                    full_num, x1 = get_full_num(idx, l[idx:])
                    nums.append([idx, x1, row, full_num])
                    idx = x1+1
                elif l[idx] in '!@#$%^&*()/+=-':
                    symbols.add((idx, row))
                    idx += 1
                else:
                    idx += 1
    
    for x0, x1, y, full_num in nums:
        neighbors = get_neighbors(x0, x1, y)
        for n in neighbors:
            if n in symbols:
                total += full_num
    
    return total

def part2(fname):
    total = 0
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

        # nums is a list of [x0, x1, y, value] lists
        nums = []

        # symbols is a set of (x,y) tuples of each * symbol location
        symbols = set()

        for row, l in enumerate(lines):
            idx = 0
            while idx < len(l):
                if isint(l[idx]):
                    full_num, x1 = get_full_num(idx, l[idx:])
                    nums.append([idx, x1, row, full_num])
                    idx = x1+1
                elif l[idx] in '*':
                    symbols.add((idx, row))
                    idx += 1
                else:
                    idx += 1
    
    for nx, ny in symbols:
        nearby_nums = 0
        subtotals = []
        neighbors = get_neighbors(nx, nx, ny)
        for x0, x1, y, full_num in nums:
            for x in range(x0, x1+1):
                if (x, y) in neighbors:
                    subtotals.append(full_num)
                    nearby_nums += 1
                    break
        if len(subtotals) == 2:
            total += (subtotals[0] * subtotals[1])
    
    return total

print(part1('input/3.txt'))
print(part2('input/3.txt'))