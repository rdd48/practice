def check_line_zeros(l):
    for i in l:
        if i:
            return True
    return False

def get_line_diff(l):
    diff = []
    for idx, val in enumerate(l[:-1]):
        diff.append(l[idx+1] - val)
    return diff

def part1(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    histories = [[int(i) for i in l.split()] for l in lines]
    
    total = 0
    for h in histories:
        curr = [h.copy()]
        while check_line_zeros(curr[-1]):
            curr.append(get_line_diff(curr[-1]))
        
        curr[-1] = curr[-1] + [0]
        # loop backwards but stop before the first line
        for i in range(len(curr)-1, 0, -1):
            val1 = curr[i][-1]
            val2 = curr[i-1][-1]
            curr[i-1] = curr[i-1] + [val1+val2]
        
        total += curr[0][-1]
        # for c in curr:
        #     print(' '.join([str(b) for b in c]))

    return total

def part2(fname):
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    histories = [[int(i) for i in l.split()] for l in lines]
    
    total = 0
    for h in histories:
        curr = [h.copy()]
        while check_line_zeros(curr[-1]):
            curr.append(get_line_diff(curr[-1]))
        
        curr[-1] = [0] + curr[-1]
        # loop backwards but stop before the first line
        for i in range(len(curr)-1, 0, -1):
            val1 = curr[i][0]
            val2 = curr[i-1][0]
            curr[i-1] = [val2-val1] + curr[i-1]
        
        total += curr[0][0]
        # for c in curr:
        #     print(' '.join([str(b) for b in c]))

    return total

print(part1('input/9.txt'))
print(part2('input/9.txt'))