def part1(fname):
    
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        times = [int(i) for i in lines[0].split()[1:]]
        dists = [int(i) for i in lines[1].split()[1:]]
    
    race_wins = [0] * len(times)

    race_no = 0
    for t,d in zip(times, dists):
        for ms_charging in range(t):
            my_dist = ms_charging * (t-ms_charging)
            if my_dist > d:
                race_wins[race_no] += 1
        race_no += 1

    ans = 1
    for i in race_wins:
        ans *= i
    
    return ans

def part2(fname):
    
    with open(fname) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        t = int(''.join([i for i in lines[0] if i in '0123456789']))
        d = int(''.join([i for i in lines[1] if i in '0123456789']))
    
    ans = 0
    for ms_charging in range(t):
        my_dist = ms_charging * (t-ms_charging)
        if my_dist > d:
            ans += 1

    return ans

print(part1('input/test.txt'))
print(part1('input/6.txt'))

print(part2('input/test.txt'))
print(part2('input/6.txt'))